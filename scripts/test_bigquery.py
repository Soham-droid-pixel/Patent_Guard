"""
Test BigQuery connection and query a few patents.
Run this to verify your BigQuery setup is working.
"""
import sys
import os

# Add parent directory to path for imports
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
backend_dir = os.path.join(parent_dir, 'backend')
sys.path.insert(0, backend_dir)

print("=" * 60)
print("Testing BigQuery Connection")
print("=" * 60)

try:
    from google.cloud import bigquery
    print("✓ google-cloud-bigquery installed")
    
    # Try to create client - read project from credentials
    try:
        import json
        # Read the project from ADC credentials
        adc_path = os.path.expanduser("~\\AppData\\Roaming\\gcloud\\application_default_credentials.json")
        project_id = None
        
        if os.path.exists(adc_path):
            with open(adc_path, 'r') as f:
                creds_data = json.load(f)
                project_id = creds_data.get('quota_project_id')
        
        if project_id:
            client = bigquery.Client(project=project_id)
            print(f"✓ BigQuery client created successfully")
            print(f"  Project: {client.project}")
        else:
            client = bigquery.Client()
            print(f"✓ BigQuery client created successfully")
            print(f"  Project: {client.project}")
    except Exception as e:
        print(f"❌ Failed to create BigQuery client")
        print(f"   Error: {e}")
        print("\n📝 Next steps:")
        print("   1. Install gcloud CLI: https://cloud.google.com/sdk/docs/install")
        print("   2. Run: gcloud auth application-default login")
        print("   3. Run: gcloud config set project YOUR-PROJECT-ID")
        sys.exit(1)
    
    # Try to query patents
    print("\nQuerying BigQuery public patents dataset...")
    query = """
    SELECT 
        publication_number,
        title_localized[SAFE_OFFSET(0)].text as title
    FROM 
        `patents-public-data.patents.publications`
    WHERE 
        country_code = 'US'
        AND ARRAY_LENGTH(title_localized) > 0
        AND publication_date >= 20240101
    ORDER BY 
        publication_date DESC
    LIMIT 5
    """
    
    query_job = client.query(query)
    results = query_job.result()
    
    patents = list(results)
    print(f"✓ Successfully queried {len(patents)} patents")
    
    if patents:
        print("\nSample patents:")
        for i, patent in enumerate(patents, 1):
            print(f"  {i}. {patent.publication_number}: {patent.title[:60]}...")
    
    print("\n" + "=" * 60)
    print("✅ BigQuery is working correctly!")
    print("=" * 60)
    print("\n🚀 You can now run: python ingest_patents.py")
    
except ImportError:
    print("❌ google-cloud-bigquery not installed")
    print("   Run: pip install google-cloud-bigquery")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ Unexpected error: {e}")
    print("\n📝 Check BIGQUERY_AUTHENTICATION.md for setup instructions")
    sys.exit(1)
