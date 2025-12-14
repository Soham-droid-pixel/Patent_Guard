"""API routes for PatentGuard."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.pinecone_svc import pinecone_service
from app.services.llm_svc import llm_service
from app.services.embedding_svc import embedding_service
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


class AnalyzeRequest(BaseModel):
    """Request model for patent analysis."""
    invention_idea: str


class AnalyzeResponse(BaseModel):
    """Response model for patent analysis."""
    risk_level: str
    analysis: str
    conflicting_patents: list
    recommendations: str
    retrieved_patents: list


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_invention(request: AnalyzeRequest):
    """
    Analyze an invention idea against prior art patents.
    
    1. Generate embedding for user's idea
    2. Query Pinecone for similar patents
    3. Use LLM to analyze and generate risk assessment
    """
    try:
        if not request.invention_idea or len(request.invention_idea.strip()) < 10:
            raise HTTPException(
                status_code=400, 
                detail="Invention idea must be at least 10 characters long"
            )
        
        logger.info(f"Analyzing invention idea: {request.invention_idea[:100]}...")
        
        # Step 1: Generate embedding for user's idea
        logger.info("Generating embedding...")
        query_embedding = embedding_service.generate_embedding(request.invention_idea)
        
        # Step 2: Query Pinecone for similar patents
        logger.info("Querying Pinecone for similar patents...")
        results = pinecone_service.query_similar(query_embedding, top_k=5)
        
        if not results.get('matches'):
            raise HTTPException(
                status_code=404,
                detail="No similar patents found. Please ensure the database has been populated."
            )
        
        # Extract patent information
        retrieved_patents = []
        for match in results['matches']:
            patent_info = {
                'id': match['id'],
                'score': match['score'],
                'metadata': match.get('metadata', {})
            }
            retrieved_patents.append(patent_info)
        
        # Step 3: Use LLM to analyze
        logger.info("Analyzing with LLM...")
        analysis_result = llm_service.analyze_patents(
            user_idea=request.invention_idea,
            retrieved_patents=retrieved_patents
        )
        
        # Prepare response
        response = AnalyzeResponse(
            risk_level=analysis_result.get('risk_level', 'Medium'),
            analysis=analysis_result.get('analysis', ''),
            conflicting_patents=analysis_result.get('conflicting_patents', []),
            recommendations=analysis_result.get('recommendations', ''),
            retrieved_patents=retrieved_patents
        )
        
        logger.info(f"Analysis complete. Risk level: {response.risk_level}")
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error during analysis: {e}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "PatentGuard API"}
