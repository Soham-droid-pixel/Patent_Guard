# BigQuery Setup Steps for PatentGuard

## 🚀 Quick Setup (Choose One Method)

### Method 1: Using gcloud CLI (Recommended - Easiest)

#### Step 1: Install gcloud CLI
1. Download from: https://cloud.google.com/sdk/docs/install
2. Run the installer
3. Restart your terminal

#### Step 2: Authenticate
```powershell
# Login to Google Cloud
gcloud auth application-default login

# This will open browser for login
# Choose your Google account
# Grant permissions
```

#### Step 3: Set Project (Create if needed)
```powershell
# Create a new free project (if you don't have one)
# Go to: https://console.cloud.google.com/projectcreate

# Then set it as default
gcloud config set project YOUR-PROJECT-ID
```

#### Step 4: Enable BigQuery API
```powershell
gcloud services enable bigquery.googleapis.com
```

#### Step 5: Test Connection
```powershell
cd C:\Users\soham\OneDrive\Desktop\PatentGuard\scripts
python test_bigquery.py
```

---

### Method 2: Using Service Account (Advanced)

#### Step 1: Create Service Account
1. Go to: https://console.cloud.google.com/iam-admin/serviceaccounts
2. Click "Create Service Account"
3. Name: `patentguard-service`
4. Click "Create and Continue"

#### Step 2: Grant Permissions
- Role: **BigQuery User**
- Click "Continue" → "Done"

#### Step 3: Create Key
1. Click on the service account you just created
2. Go to "Keys" tab
3. Click "Add Key" → "Create new key"
4. Choose "JSON"
5. Save the downloaded file

#### Step 4: Update .env
```bash
# Copy the JSON file to your project
# Then update backend/.env:
GOOGLE_APPLICATION_CREDENTIALS=C:/path/to/your-service-account-key.json
GOOGLE_CLOUD_PROJECT=your-project-id
```

---

## ✅ Verification

After setup, run:
```powershell
cd scripts
python test_bigquery.py
```

You should see:
```
✓ BigQuery connection successful!
✓ Found X patents in public dataset
```

## 🎯 Next Steps

Once BigQuery is working:
```powershell
# Populate Pinecone with patent data
cd scripts
python ingest_patents.py
```

This will:
- Fetch 50 recent US patents from BigQuery
- Generate embeddings
- Upload to Pinecone
- Takes about 2-3 minutes

## 💰 Cost Info

- BigQuery public data queries: **FREE** (up to 1TB/month)
- Google Cloud Project: **FREE** (no credit card required initially)
- The queries in this project use ~1MB, well within free tier

## 🆘 Troubleshooting

### "gcloud not found"
- Install gcloud CLI from the link above
- Restart terminal after installation

### "Permission denied"
- Make sure you granted BigQuery User role
- Re-run: `gcloud auth application-default login`

### "Project not set"
- Create project at: https://console.cloud.google.com/projectcreate
- Run: `gcloud config set project YOUR-PROJECT-ID`

### Still not working?
- Check if BigQuery API is enabled: https://console.cloud.google.com/apis/library/bigquery.googleapis.com
- Make sure you're using the correct project ID (not project name)
