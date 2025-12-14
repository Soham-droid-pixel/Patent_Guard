"""Main FastAPI application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.core.config import settings
from app.services.pinecone_svc import pinecone_service
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="PatentGuard API",
    description="Patent Prior Art Search Engine API",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router, prefix="/api")


@app.on_event("startup")
async def startup_event():
    """Initialize services on startup."""
    logger.info("Starting PatentGuard API...")
    try:
        # Initialize Pinecone connection
        pinecone_service.initialize_index()
        logger.info("Pinecone initialized successfully")
    except Exception as e:
        logger.error(f"Error during startup: {e}")
        logger.warning("Some services may not be available")


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to PatentGuard API",
        "version": "1.0.0",
        "docs": "/docs"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=True
    )
