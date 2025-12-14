# BigQuery Setup for PatentGuard

## Quick Setup (5 minutes)

### Step 1: Create a Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Create Project" or select an existing project
3. Note your **Project ID** (e.g., `my-patent-project-123`)

### Step 2: Enable BigQuery API
1. In the Cloud Console, go to "APIs & Services" → "Library"
2. Search for "BigQuery API"
3. Click "Enable"

### Step 3: Authenticate
You have two options:

#### Option A: Application Default Credentials (Recommended)
```bash
# Install gcloud CLI if not installed
# Download from: https://cloud.google.com/sdk/docs/install

# Login to your Google account
gcloud auth application-default login

# Set your project
gcloud config set project YOUR-PROJECT-ID
```

#### Option B: Service Account (Advanced)
1. Go to "IAM & Admin" → "Service Accounts"
2. Create a service account
3. Grant "BigQuery User" role
4. Create and download JSON key
5. Set path in `.env`:
   ```
   GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json
   ```

### Step 4: Update .env File
```bash
cd backend
# Edit .env and add your project ID
GOOGLE_CLOUD_PROJECT=your-actual-project-id
```

### Step 5: Test Connection
```bash
cd scripts
python ingest_patents.py
```

## Important Notes
- BigQuery public datasets are **FREE to query** (up to 1TB/month)
- The patents dataset is publicly accessible
- You only need a GCP project for billing identity
- No charges for the queries in this project (well within free tier)

## Troubleshooting

### Error: "File not found"
- Use Option A (gcloud auth) - easier and recommended

### Error: "Project not found"
- Make sure project ID in .env matches your GCP project
- Project ID is NOT the same as project name

### Error: "API not enabled"
- Enable BigQuery API in Cloud Console

## Alternative: Use Sample Data
If you want to skip BigQuery setup for now, the script automatically falls back to sample patent data when BigQuery is unavailable.
