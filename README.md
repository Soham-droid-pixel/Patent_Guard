# PatentGuard 🛡️

An AI-powered Patent Prior Art Search Engine that helps inventors quickly assess whether their ideas conflict with existing patents. Built with modern technologies and running entirely on free-tier services.

## ✨ Features

- **Semantic Patent Search**: Uses state-of-the-art embeddings to find semantically similar patents beyond keyword matching
- **AI Risk Assessment**: Analyzes potential conflicts and assigns risk levels (High/Medium/Low)
- **Real Patent Data**: Searches through Google's public patent dataset via BigQuery
- **Detailed Analysis**: Get professional-grade conflict analysis powered by Groq's LLM
- **Modern UI**: Clean, responsive interface built with React and Tailwind CSS

## 🚀 Tech Stack (100% Free Tier)

- **Frontend:** React 19 + Vite + Tailwind CSS
- **Backend:** Python 3.11+ with FastAPI
- **Vector Database:** Pinecone Serverless (Free Tier)
- **Data Source:** Google BigQuery (Public Patent Dataset)
- **LLM:** Groq API with Llama 3.3 70B
- **Embeddings:** sentence-transformers/all-MiniLM-L6-v2 (Local)

## 📦 Project Structure

```
patent-guard/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── prompts.py
│   │   ├── services/
│   │   │   ├── pinecone_svc.py
│   │   │   ├── bigquery_svc.py
│   │   │   ├── llm_svc.py
│   │   │   └── embedding_svc.py
│   │   └── main.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── SearchInput.jsx
│   │   │   └── ResultsDisplay.jsx
│   │   ├── api/
│   │   │   └── client.js
│   │   └── App.jsx
│   └── package.json
└── scripts/
    └── ingest_patents.py
```

## 🛠️ Quick Start

### Prerequisites

- **Python 3.11+** with pip
- **Node.js 18+** with npm
- **Pinecone Account**: Free tier at [pinecone.io](https://www.pinecone.io/)
- **Groq API Key**: Free tier at [console.groq.com](https://console.groq.com/)
- **Google Cloud**: For BigQuery access (free public dataset access via gcloud CLI)

### 1. Clone & Setup Environment

```bash
git clone <your-repo-url>
cd PatentGuard

# Activate virtual environment (Windows)
venv\Scripts\activate

# Or on Mac/Linux
source venv/bin/activate
```

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt

# Create .env file with your API keys
# NEVER commit this file to Git!
```

**backend/.env** (create this file):
```env
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_INDEX_NAME=patentguard
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_APPLICATION_CREDENTIALS=app/service-account.json
HOST=0.0.0.0
PORT=8000
```

### 3. Google Cloud Authentication

**Option A: Using gcloud CLI (Recommended)**
```bash
# Install gcloud CLI from https://cloud.google.com/sdk/docs/install
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
```

**Option B: Service Account**
- Download service account JSON from Google Cloud Console
- Place it at `backend/app/service-account.json`
- Update `GOOGLE_APPLICATION_CREDENTIALS` in .env

### 4. Ingest Patent Data

```bash
# From project root
python scripts/ingest_patents.py
```

This fetches 50 recent patents from BigQuery and stores them in Pinecone.

### 5. Start Backend Server

```bash
cd backend
python -m uvicorn app.main:app --reload
```

Backend runs at `http://localhost:8000` (API docs at `/docs`)

### 6. Start Frontend

```bash
# In a new terminal
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173` (or 5174 if 5173 is busy)

## 🎯 How to Use

1. Open your browser to `http://localhost:5173`
2. Enter a detailed description of your invention idea (minimum 20 characters)
3. Click **"Analyze for Prior Art"**
4. Get instant results:
   - **Risk Level**: High/Medium/Low conflict assessment
   - **Similar Patents**: Top matching patents with similarity scores
   - **Detailed Analysis**: Professional conflict analysis and recommendations

## 🏗️ Architecture

```
User Input → Embedding Service (Local) → Pinecone Vector Search 
           ↓
Similar Patents → Groq LLM Analysis → Risk Assessment + Recommendations
```

**Key Components:**
- **Embedding Service**: Converts text to 384-dimensional vectors using sentence-transformers
- **Pinecone**: Stores and queries patent vectors with cosine similarity
- **BigQuery**: Sources patent data from Google's public dataset
- **Groq LLM**: Analyzes conflicts and generates professional reports

## 🔧 API Reference

**POST** `/api/analyze`
```json
{
  "invention_idea": "A smart water bottle that tracks hydration"
}
```

**Response:**
```json
{
  "risk_level": "Medium",
  "conflict_analysis": "Detailed analysis...",
  "similar_patents": [
    {
      "publication_number": "US-20250001234-A1",
      "title": "...",
      "similarity_score": 0.87
    }
  ]
}
```

## ⚙️ Configuration

All configuration is managed through environment variables in `backend/.env`:

| Variable | Description | Required |
|----------|-------------|----------|
| `PINECONE_API_KEY` | Your Pinecone API key | ✅ |
| `PINECONE_INDEX_NAME` | Name of your Pinecone index | ✅ |
| `GROQ_API_KEY` | Your Groq API key | ✅ |
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to service account JSON | ❌ (if using gcloud) |
| `HOST` | Backend host | Optional (default: 0.0.0.0) |
| `PORT` | Backend port | Optional (default: 8000) |

## 🚨 Important Security Notes

- **NEVER** commit `.env` file or service account JSON to Git
- The `.gitignore` file is configured to exclude all sensitive files
- Always use environment variables for secrets
- Review files before pushing to GitHub

## 📝 Development Notes

- Patent embeddings are 384-dimensional vectors
- Ingestion script fetches 50 recent US patents by default (configurable)
- Similarity threshold for relevant patents: 0.7+ (high relevance)
- BigQuery uses public dataset: `patents-public-data.patents.publications`

## 🤝 Contributing

This is an MVP project built for learning and demonstration. Contributions welcome!

**Areas for improvement:**
- Add user authentication
- Implement caching for common queries
- Expand to international patents
- Add patent visualization features
- Improve UI/UX with charts and graphs

## 📄 License

MIT License - Free to use and modify

## 🙏 Acknowledgments

- Google BigQuery for public patent dataset
- Pinecone for vector database free tier
- Groq for fast LLM inference
- HuggingFace for sentence-transformers

---

**Built with ❤️ for inventors and innovators**
