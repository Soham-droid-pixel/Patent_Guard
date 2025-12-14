# PatentGuard - Quick Start Guide

## ✅ Prerequisites Completed
- ✓ Backend structure created
- ✓ Frontend React app created with Vite + Tailwind
- ✓ All services implemented
- ✓ Virtual environment (venv) set up

## 🚀 Running the Application

### Terminal 1: Start Backend

```powershell
# Activate virtual environment
cd C:\Users\soham\OneDrive\Desktop\PatentGuard
venv\Scripts\activate

# Install backend dependencies (if not done)
cd backend
pip install -r requirements.txt

# Start the FastAPI server
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will run at: `http://localhost:8000`
API docs at: `http://localhost:8000/docs`

### Terminal 2: Start Frontend

```powershell
# Navigate to frontend
cd C:\Users\soham\OneDrive\Desktop\PatentGuard\frontend

# Install dependencies (if not done)
npm install

# Start Vite dev server
npm run dev
```

Frontend will run at: `http://localhost:5173`

## 🎯 Testing the Application

1. **Open browser**: Go to `http://localhost:5173`
2. **Enter invention idea**: Type a detailed description (min 10 characters)
3. **Click "Analyze for Prior Art"**: Wait for AI analysis
4. **View results**: See risk level and similar patents

## 📊 Sample Invention Ideas to Test

Try these:
```
A smart water bottle that tracks hydration levels and sends reminders through LED lights and a mobile app
```

```
A wearable device that monitors heart rate and sends alerts to doctors when abnormal patterns are detected
```

## ⚠️ Common Issues & Solutions

### Backend won't start
- **Issue**: Module not found errors
- **Fix**: Make sure venv is activated and dependencies installed
  ```powershell
  venv\Scripts\activate
  cd backend
  pip install -r requirements.txt
  ```

### Frontend shows blank page
- **Issue**: Backend not running
- **Fix**: Start backend first (see Terminal 1 above)

### "No similar patents found" error
- **Issue**: Pinecone index is empty
- **Fix**: Run ingestion script to populate data
  ```powershell
  venv\Scripts\activate
  cd scripts
  python ingest_patents.py
  ```

### CORS errors in browser
- **Issue**: Backend CORS not configured for frontend URL
- **Fix**: Already configured for `http://localhost:5173` ✓

## 🔑 API Keys Status

Check your `.env` file in backend folder:
- ✅ Pinecone API Key: Configured
- ✅ Groq API Key: Configured
- ⚠️ Google Cloud: Optional (uses sample data if not configured)

## 📝 Next Steps

1. **Test with sample data** (works without BigQuery)
2. **Run ingestion script** to populate real patent data
3. **Try different invention ideas** to see AI analysis
4. **Check API docs** at `http://localhost:8000/docs`

## 🆘 Need Help?

- Backend logs: Check terminal running uvicorn
- Frontend errors: Open browser console (F12)
- API testing: Use `http://localhost:8000/docs` (Swagger UI)
