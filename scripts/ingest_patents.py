"""
Patent Data Ingestion Script
Fetches patents from Google BigQuery and uploads them to Pinecone.
"""
import sys
import os

# Add parent directory to path for imports
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
backend_dir = os.path.join(parent_dir, 'backend')
sys.path.insert(0, backend_dir)

from app.services.bigquery_svc import bigquery_service
from app.services.pinecone_svc import pinecone_service
from app.services.embedding_svc import embedding_service
from app.core.config import settings
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_sample_patents():
    """Return sample patent data for testing when BigQuery is not available."""
    return [
        {
            "publication_number": "US-2023-0001234-A1",
            "title": "Smart Hydration Tracking Device with LED Indicators",
            "abstract": "A portable water bottle equipped with sensors to monitor water intake and display hydration levels through integrated LED lights. The device connects to a mobile application via Bluetooth to provide personalized hydration reminders based on user activity levels.",
            "publication_date": "2023-01-15"
        },
        {
            "publication_number": "US-2023-0005678-A1",
            "title": "Wearable Health Monitoring System with Real-Time Alerts",
            "abstract": "A wearable device that continuously monitors vital signs including heart rate, blood pressure, and temperature. The system uses machine learning algorithms to detect anomalies and send immediate alerts to users and healthcare providers.",
            "publication_date": "2023-02-20"
        },
        {
            "publication_number": "US-2023-0009012-A1",
            "title": "Automated Plant Care System with Soil Moisture Sensors",
            "abstract": "An intelligent plant care device featuring soil moisture sensors, automated watering mechanisms, and smartphone connectivity. The system learns plant watering schedules and adjusts based on environmental conditions.",
            "publication_date": "2023-03-10"
        },
        {
            "publication_number": "US-2023-0003456-A1",
            "title": "Voice-Activated Smart Home Energy Management System",
            "abstract": "A comprehensive home energy management solution that uses voice commands and AI to optimize energy consumption. The system integrates with smart appliances and learns usage patterns to reduce electricity costs.",
            "publication_date": "2023-04-05"
        },
        {
            "publication_number": "US-2023-0007890-A1",
            "title": "Portable Air Quality Monitor with Mobile Notifications",
            "abstract": "A compact device for measuring indoor air quality including CO2, VOCs, and particulate matter. Features real-time data display and sends alerts to users' smartphones when air quality deteriorates.",
            "publication_date": "2023-05-12"
        }
    ]


def main():
    """Main ingestion process."""
    try:
        logger.info("=" * 60)
        logger.info("Starting Patent Ingestion Process")
        logger.info("=" * 60)
        
        # Step 1: Initialize Pinecone
        logger.info("\n[1/4] Initializing Pinecone...")
        pinecone_service.initialize_index()
        logger.info("✓ Pinecone initialized")
        
        # Step 2: Fetch patents from BigQuery or use sample data
        logger.info("\n[2/4] Fetching patents...")
        
        if bigquery_service.client:
            logger.info("Using BigQuery for patent data...")
            patents = bigquery_service.fetch_recent_patents(limit=50)
        else:
            logger.warning("BigQuery not available. Using sample patent data...")
            patents = get_sample_patents()
        
        logger.info(f"✓ Fetched {len(patents)} patents")
        
        if not patents:
            logger.error("No patents available. Exiting.")
            return
        
        # Step 3: Generate embeddings
        logger.info("\n[3/4] Generating embeddings...")
        vectors_to_upsert = []
        
        for i, patent in enumerate(patents):
            # Combine title and abstract for embedding
            text_to_embed = f"{patent['title']} {patent['abstract']}"
            
            # Generate embedding
            embedding = embedding_service.generate_embedding(text_to_embed)
            
            # Prepare vector for Pinecone
            vector = {
                'id': patent['publication_number'],
                'values': embedding,
                'metadata': {
                    'publication_number': patent['publication_number'],
                    'title': patent['title'][:500],  # Limit metadata size
                    'abstract': patent['abstract'][:1000],
                    'publication_date': patent['publication_date']
                }
            }
            vectors_to_upsert.append(vector)
            
            if (i + 1) % 10 == 0:
                logger.info(f"  Processed {i + 1}/{len(patents)} patents...")
        
        logger.info(f"✓ Generated {len(vectors_to_upsert)} embeddings")
        
        # Step 4: Upload to Pinecone
        logger.info("\n[4/4] Uploading to Pinecone...")
        batch_size = 100
        for i in range(0, len(vectors_to_upsert), batch_size):
            batch = vectors_to_upsert[i:i + batch_size]
            pinecone_service.upsert_vectors(batch)
            logger.info(f"  Uploaded batch {i//batch_size + 1}")
        
        logger.info("✓ All vectors uploaded to Pinecone")
        
        logger.info("\n" + "=" * 60)
        logger.info("INGESTION COMPLETE!")
        logger.info(f"Total patents ingested: {len(patents)}")
        logger.info("=" * 60)
        
    except Exception as e:
        logger.error(f"\n❌ Error during ingestion: {e}")
        raise


if __name__ == "__main__":
    main()
