"""Google BigQuery service for patent data."""
from google.cloud import bigquery
from app.core.config import settings
from typing import List, Dict, Any
import logging
import os

logger = logging.getLogger(__name__)


class BigQueryService:
    """Service for querying patent data from Google BigQuery."""
    
    def __init__(self):
        # Try to initialize BigQuery client with available credentials
        # Priority: 1) Service account file, 2) Application default credentials
        
        # First try: Service account JSON file (if provided)
        if settings.google_credentials:
            # Remove quotes if present
            cred_path = settings.google_credentials.strip('"').strip("'")
            
            # Try as absolute path first
            if not os.path.isabs(cred_path):
                # Make it relative to the project root (parent of backend)
                backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                project_root = os.path.dirname(backend_dir)
                cred_path = os.path.join(project_root, cred_path)
            
            if os.path.exists(cred_path):
                try:
                    self.client = bigquery.Client.from_service_account_json(cred_path)
                    logger.info(f"✓ BigQuery initialized with service account: {cred_path}")
                    logger.info(f"  Project: {self.client.project}")
                    return
                except Exception as e:
                    logger.error(f"Failed to load service account from {cred_path}: {e}")
            else:
                logger.warning(f"Service account file not found: {cred_path}")
        
        # Second try: Application default credentials from gcloud
        try:
            import json
            adc_path = os.path.expanduser("~\\AppData\\Roaming\\gcloud\\application_default_credentials.json")
            project_id = None
            
            if os.path.exists(adc_path):
                with open(adc_path, 'r') as f:
                    creds_data = json.load(f)
                    project_id = creds_data.get('quota_project_id')
            
            if project_id:
                self.client = bigquery.Client(project=project_id)
                logger.info(f"✓ BigQuery initialized with ADC, project: {project_id}")
            else:
                self.client = bigquery.Client()
                logger.info(f"✓ BigQuery initialized with project: {self.client.project}")
        except Exception as e:
            self.client = None
            logger.error(f"❌ Failed to initialize BigQuery: {e}")
            logger.info("💡 Options: 1) Add service-account.json, 2) Run: gcloud auth application-default login")
    
    def fetch_recent_patents(self, limit: int = 50) -> List[Dict[str, Any]]:
        """
        Fetch recent US patents from BigQuery public dataset.
        
        Args:
            limit: Number of patents to fetch
            
        Returns:
            List of patent dictionaries
        """
        query = f"""
        SELECT 
            publication_number,
            title_localized[SAFE_OFFSET(0)].text as title,
            abstract_localized[SAFE_OFFSET(0)].text as abstract,
            claims_localized[SAFE_OFFSET(0)].text as claims,
            publication_date
        FROM 
            `patents-public-data.patents.publications`
        WHERE 
            country_code = 'US'
            AND ARRAY_LENGTH(title_localized) > 0
            AND ARRAY_LENGTH(abstract_localized) > 0
            AND publication_date >= 20230101
        ORDER BY 
            publication_date DESC
        LIMIT {limit}
        """
        
        if not self.client:
            logger.error("BigQuery client is not available. Cannot fetch patents.")
            raise Exception("BigQuery is not configured. Please set up Google Cloud credentials.")
        
        try:
            query_job = self.client.query(query)
            results = query_job.result()
            
            patents = []
            for row in results:
                patent = {
                    "publication_number": row.publication_number,
                    "title": row.title or "",
                    "abstract": row.abstract or "",
                    "claims": row.claims or "",
                    "publication_date": str(row.publication_date) if row.publication_date else ""
                }
                patents.append(patent)
            
            logger.info(f"Fetched {len(patents)} patents from BigQuery")
            return patents
            
        except Exception as e:
            logger.error(f"Error fetching patents from BigQuery: {e}")
            raise


# Singleton instance
bigquery_service = BigQueryService()
