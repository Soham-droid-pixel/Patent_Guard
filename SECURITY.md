# Security Guidelines 🔒

## Critical: Protecting Sensitive Data

This project uses several API keys and credentials that **MUST NEVER** be committed to version control or shared publicly.

## 🚨 Never Commit These Files

The `.gitignore` is configured to exclude:

### Environment Files
- `.env` (contains all API keys)
- `.env.local`
- `.env.production`
- Any file matching `*.env` pattern

### Credential Files
- `service-account.json` or `service-account-*.json`
- `application_default_credentials.json`
- Any file matching `*credentials*.json`
- Any file matching `*key*.json`

### API Keys & Secrets
- Files containing `secret`, `password`, `token`, `apikey` in their names

### Large Datasets
- `*.csv`, `*.parquet` files
- `datasets/` or `data/` directories
- Any downloaded patent data

## ✅ Before Pushing to GitHub

**Checklist:**

1. **Verify .gitignore is present** ✓
2. **Ensure .env file is NOT in git**
   ```bash
   git status
   # Should NOT see backend/.env
   ```

3. **Check for service account files**
   ```bash
   # These should NOT appear in git status
   # - backend/app/service-account.json
   # - Any *credentials*.json files
   ```

4. **Verify package.json and requirements.txt are included** ✓
   - These are safe to commit (no secrets)

5. **Check .env.example is included** ✓
   - Template file is safe and helpful

## 🔑 API Keys Used

This project requires the following API keys (stored in `.env`):

| Service | Purpose | Free Tier? |
|---------|---------|------------|
| **Pinecone** | Vector database for patent embeddings | ✅ Yes (serverless) |
| **Groq** | LLM for patent analysis | ✅ Yes (rate limited) |
| **Google Cloud** | BigQuery for patent data | ✅ Yes (1TB queries/month) |

## 🛡️ Setting Up Secrets Securely

### 1. Create .env File (NEVER commit this!)

```bash
cd backend
cp .env.example .env
# Edit .env with your actual API keys
```

### 2. Google Cloud Authentication

**Option A: Using gcloud CLI (Recommended)**
```bash
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
```

This stores credentials at:
- Windows: `%APPDATA%\gcloud\application_default_credentials.json`
- Mac/Linux: `~/.config/gcloud/application_default_credentials.json`

These paths are **already excluded** by .gitignore.

**Option B: Service Account**
1. Download service account JSON from Google Cloud Console
2. Save as `backend/app/service-account.json`
3. Update `.env`: `GOOGLE_APPLICATION_CREDENTIALS=app/service-account.json`
4. Verify it's excluded: `git status` should NOT show this file

## 🔍 What If I Accidentally Commit Secrets?

If you accidentally commit API keys or credentials:

1. **Immediately rotate/regenerate all exposed keys**
   - Pinecone: Regenerate API key in dashboard
   - Groq: Create new API key and delete old one
   - Google Cloud: Revoke service account and create new one

2. **Remove from Git history**
   ```bash
   # For recent commit (not pushed)
   git reset --soft HEAD~1
   git restore --staged .env
   
   # If already pushed, you MUST rotate keys
   # Consider using git-filter-branch or BFG Repo-Cleaner
   ```

3. **Verify .gitignore before next commit**

## 📁 Directory Structure (Security Perspective)

```
PatentGuard/
├── .gitignore              ✅ Commit (protects secrets)
├── .env.example            ✅ Commit (template only)
├── backend/
│   ├── .env                ❌ NEVER COMMIT (has real keys)
│   ├── app/
│   │   └── service-account.json  ❌ NEVER COMMIT
│   └── requirements.txt    ✅ Commit (no secrets)
├── frontend/
│   ├── package.json        ✅ Commit (no secrets)
│   └── .env                ❌ NEVER COMMIT (if created)
└── README.md               ✅ Commit (public info only)
```

## 🚀 For Contributors

If you fork this project:

1. **Never commit your own API keys**
2. **Always use .env files for secrets**
3. **Test locally before pushing**
4. **Review `git diff` before committing**

## 📞 Reporting Security Issues

If you discover a security vulnerability in this codebase:
- Do NOT open a public issue
- Contact the maintainer privately
- Allow time for patching before disclosure

## 🔐 Production Deployment Notes

For production use, consider:
- Use environment variables from hosting platform (Vercel, Heroku, Railway)
- Never hardcode secrets in code
- Implement rate limiting on API endpoints
- Add authentication for public-facing APIs
- Use secrets management services (AWS Secrets Manager, etc.)

---

**Remember: Security is everyone's responsibility. When in doubt, don't commit it!** 🛡️
