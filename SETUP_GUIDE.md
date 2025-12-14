# 🚀 Complete Setup Guide - BigQuery + Groq

## ✅ Status Check

### Groq API: ✓ WORKING
- Model: `llama-3.3-70b-versatile`
- Your API key is valid and working!

### BigQuery: ⚠️ NEEDS SETUP
You need to authenticate with Google Cloud to access BigQuery public patents data.

---

## 📋 BigQuery Setup (10 minutes)

### Option 1: Quick Setup with gcloud CLI (Recommended)

#### Step 1: Download & Install gcloud CLI
1. **Download**: https://cloud.google.com/sdk/docs/install-sdk#windows
2. Click "Download the Google Cloud CLI installer"
3. Run the installer (GoogleCloudSDKInstaller.exe)
4. **Important**: Check "Run 'gcloud init'" at the end
5. Close and reopen your PowerShell terminal

#### Step 2: Initialize gcloud
```powershell
# This command will open your browser
gcloud init

# Follow these steps in the browser:
# 1. Choose your Google account (any Gmail account works)
# 2. Click "Allow" to grant permissions
# 3. In terminal, create a new project or select existing one
# 4. Choose a region (any is fine, e.g., us-central1)
```

#### Step 3: Set up Application Default Credentials
```powershell
gcloud auth application-default login
```
This opens browser again - just click "Allow"

#### Step 4: Enable BigQuery API
```powershell
gcloud services enable bigquery.googleapis.com
```

#### Step 5: Test BigQuery
```powershell
cd C:\Users\soham\OneDrive\Desktop\PatentGuard\scripts
python test_bigquery.py
```

You should see: ✅ BigQuery is working correctly!

---

### Option 2: Without gcloud (Alternative - Service Account)

If you can't install gcloud, you can use a service account:

#### Step 1: Create Google Cloud Project
1. Go to: https://console.cloud.google.com/projectcreate
2. Project name: `patentguard`
3. Click "Create"
4. Note your **Project ID** (shown in parentheses)

#### Step 2: Enable BigQuery API
1. Go to: https://console.cloud.google.com/apis/library/bigquery.googleapis.com
2. Select your project
3. Click "Enable"

#### Step 3: Create Service Account
1. Go to: https://console.cloud.google.com/iam-admin/serviceaccounts
2. Click "Create Service Account"
3. Name: `patentguard-service`
4. Click "Create and Continue"
5. Role: Select "BigQuery User"
6. Click "Continue" → "Done"

#### Step 4: Create & Download Key
1. Click on the service account you just created
2. Go to "Keys" tab
3. Click "Add Key" → "Create new key"
4. Choose **JSON**
5. Save the file as: `C:\Users\soham\OneDrive\Desktop\PatentGuard\backend\service-account.json`

#### Step 5: Update backend/.env
Open `backend/.env` and change:
```env
GOOGLE_APPLICATION_CREDENTIALS=C:/Users/soham/OneDrive/Desktop/PatentGuard/backend/service-account.json
GOOGLE_CLOUD_PROJECT=your-project-id-here
```

#### Step 6: Test
```powershell
cd C:\Users\soham\OneDrive\Desktop\PatentGuard\scripts
python test_bigquery.py
```

---

## 🎯 After BigQuery is Working

Once you see "✅ BigQuery is working correctly!", run:

```powershell
# Populate Pinecone with real patent data
cd C:\Users\soham\OneDrive\Desktop\PatentGuard\scripts
python ingest_patents.py
```

This will:
- ✓ Fetch 50 recent US patents from BigQuery
- ✓ Generate embeddings locally
- ✓ Upload to Pinecone
- ⏱️ Takes 2-3 minutes

---

## 💰 Cost Information

- **BigQuery**: FREE (up to 1TB/month, we use ~1MB)
- **Google Cloud Project**: FREE (no credit card required)
- **Groq API**: FREE tier available
- **Pinecone**: FREE tier (100k vectors)

Total cost: **$0.00** 🎉

---

## ✅ Verification

After setup, your app will:
1. Accept invention ideas from users
2. Generate embeddings locally
3. Search Pinecone for similar patents (from BigQuery data)
4. Use Groq AI (Llama 3.3) to analyze conflicts
5. Return risk assessment

---

## 🆘 Troubleshooting

### "gcloud not found" after installation
- Close and reopen PowerShell
- Or run: `C:\Users\soham\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd`

### "Permission denied" during gcloud init
- Make sure you're using a Google account (Gmail)
- Try: `gcloud auth login` first

### "Project not found"
- Use Project ID (not Project Name)
- Check at: https://console.cloud.google.com/

### Service account not working
- Make sure JSON file path uses forward slashes: `/` not `\`
- Or use double backslashes: `\\`

---

## 📞 Need Help?

Run the test scripts to diagnose issues:
```powershell
# Test Groq (already working ✓)
python test_groq.py

# Test BigQuery (needs setup)
python test_bigquery.py
```
