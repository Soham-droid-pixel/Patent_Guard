"""Pinecone vector database service."""
from pinecone import Pinecone, ServerlessSpec
from app.core.config import settings
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class PineconeService:
    """Service for interacting with Pinecone vector database."""
    
    def __init__(self):
        self.pc = Pinecone(api_key=settings.pinecone_api_key)
        self.index_name = settings.pinecone_index_name
        self.index = None
        
    def initialize_index(self):
        """Initialize or connect to existing Pinecone index."""
        try:
            # Check if index exists
            existing_indexes = [idx.name for idx in self.pc.list_indexes()]
            
            if self.index_name not in existing_indexes:
                logger.info(f"Creating new index: {self.index_name}")
                self.pc.create_index(
                    name=self.index_name,
                    dimension=settings.embedding_dimension,
                    metric="cosine",
                    spec=ServerlessSpec(
                        cloud="aws",
                        region="us-east-1"
                    )
                )
            
            self.index = self.pc.Index(self.index_name)
            logger.info(f"Connected to index: {self.index_name}")
            return True
            
        except Exception as e:
            logger.error(f"Error initializing Pinecone index: {e}")
            raise
    
    def upsert_vectors(self, vectors: List[Dict[str, Any]]):
        """
        Upsert vectors to Pinecone.
        
        Args:
            vectors: List of dicts with 'id', 'values', and 'metadata'
        """
        try:
            if not self.index:
                self.initialize_index()
            
            self.index.upsert(vectors=vectors)
            logger.info(f"Upserted {len(vectors)} vectors to Pinecone")
            
        except Exception as e:
            logger.error(f"Error upserting vectors: {e}")
            raise
    
    def query_similar(self, query_vector: List[float], top_k: int = 5) -> Dict[str, Any]:
        """
        Query for similar vectors.
        
        Args:
            query_vector: The embedding vector to search for
            top_k: Number of results to return
            
        Returns:
            Query results from Pinecone
        """
        try:
            if not self.index:
                self.initialize_index()
            
            results = self.index.query(
                vector=query_vector,
                top_k=top_k,
                include_metadata=True
            )
            
            return results
            
        except Exception as e:
            logger.error(f"Error querying Pinecone: {e}")
            raise


# Singleton instance
pinecone_service = PineconeService()
