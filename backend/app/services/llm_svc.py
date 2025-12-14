"""LLM service using Groq API."""
from groq import Groq
from app.core.config import settings
from app.core.prompts import PATENT_ANALYSIS_PROMPT
from typing import List, Dict, Any
import json
import logging

logger = logging.getLogger(__name__)


class LLMService:
    """Service for LLM inference using Groq."""
    
    def __init__(self):
        self.client = Groq(api_key=settings.groq_api_key)
        self.model = settings.groq_model
    
    def analyze_patents(
        self, 
        user_idea: str, 
        retrieved_patents: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Analyze user's invention idea against retrieved patents.
        
        Args:
            user_idea: The user's invention description
            retrieved_patents: List of similar patents from Pinecone
            
        Returns:
            Analysis results with risk level and recommendations
        """
        try:
            # Format retrieved patents for the prompt
            patents_text = ""
            for i, patent in enumerate(retrieved_patents, 1):
                metadata = patent.get('metadata', {})
                patents_text += f"\n--- Patent {i} ---\n"
                patents_text += f"Number: {metadata.get('publication_number', 'N/A')}\n"
                patents_text += f"Title: {metadata.get('title', 'N/A')}\n"
                patents_text += f"Abstract: {metadata.get('abstract', 'N/A')[:500]}...\n"
                patents_text += f"Similarity Score: {patent.get('score', 0):.3f}\n"
            
            # Create the prompt
            prompt = PATENT_ANALYSIS_PROMPT.format(
                user_idea=user_idea,
                retrieved_patents=patents_text
            )
            
            # Call Groq API
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert Patent Attorney. Always respond with valid JSON."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=self.model,
                temperature=0.3,
                max_tokens=2000
            )
            
            response_text = chat_completion.choices[0].message.content
            
            # Try to parse JSON response
            try:
                analysis = json.loads(response_text)
            except json.JSONDecodeError:
                # If not valid JSON, create structured response
                logger.warning("LLM response was not valid JSON, creating structured response")
                analysis = {
                    "risk_level": "Medium",
                    "analysis": response_text,
                    "conflicting_patents": [p.get('metadata', {}).get('publication_number', '') 
                                          for p in retrieved_patents[:3]],
                    "recommendations": "Please consult with a patent attorney for detailed analysis."
                }
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error calling Groq API: {e}")
            raise


# Singleton instance
llm_service = LLMService()
