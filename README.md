<div align="center">

# 🛡️ PatentGuard

### AI-Powered Patent Prior Art Search Engine

*Protect your innovation before it's too late*

**From observing a "Glitch" to building a "Guard."**

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![React 19](https://img.shields.io/badge/react-19-61DAFB.svg)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Features](#-features) • [Demo](#-demo) • [Quick Start](#-quick-start) • [Architecture](#-architecture) • [API](#-api-reference) • [Contributing](#-contributing)

</div>

---

## 🌟 What is PatentGuard?

PatentGuard is a revolutionary **AI-powered patent search engine** that helps inventors, entrepreneurs, and companies quickly assess whether their ideas conflict with existing patents. Using cutting-edge semantic search and AI analysis, PatentGuard provides instant, professional-grade prior art searches—**completely free**.

### 💡 The Problem We're Solving

Professional patent searches are **incredibly expensive**, often costing between **₹80,000 to ₹4,00,000+** ($1,000-$5,000+). Many independent inventors and small startups in India and around the world give up before they even start because of this heavy financial barrier.

### 🎯 The Solution

An intelligent, semantic search engine that identifies potential patent conflicts in **seconds**, for **free**. PatentGuard democratizes innovation by making professional-grade patent searches accessible to everyone.

### 💡 Why PatentGuard?

- **Save Time**: Get instant results instead of hours of manual patent searches
- **Save Money**: Professional searches cost thousands. PatentGuard is 100% free
- **Make Informed Decisions**: Understand your patent risk before investing in development
- **Powered by Real Data**: Searches through **Google's public patent dataset** (millions of patents)
- **AI Analysis**: Get expert-level insights from state-of-the-art LLMs (Groq's Llama 3.3 70B)
- **Semantic Understanding**: Goes beyond keyword matching to catch similarities traditional searches miss

---

## ✨ Features

### 🔍 **Semantic Patent Search**
Goes beyond keyword matching using **sentence-transformers** to understand the *meaning* of your invention. Finds similar patents even if they use different terminology.

### 🤖 **AI Risk Assessment**
**Groq's Llama 3.3 70B** analyzes your invention against prior art and assigns risk levels:
- 🔴 **High Risk**: Strong overlap with existing patents
- 🟡 **Medium Risk**: Some similarities but differentiable
- 🟢 **Low Risk**: Mostly novel with minimal conflicts

### 📊 **Real Patent Data**
Searches through **Google BigQuery's public patent dataset**:
- Millions of US patents
- Updated regularly with latest publications
- Includes titles, abstracts, claims, and metadata

### 📋 **Professional Analysis**
Get detailed conflict analysis including:
- Specific patent conflicts identified
- Similarity scores for each match
- Actionable recommendations
- Clear, readable reports

### 🎨 **Modern, Intuitive UI**
Built with **React 19** and **Tailwind CSS**:
- Clean, professional interface
- Responsive design (works on all devices)
- Real-time loading states
- Color-coded risk levels
- Interactive example queries

### 💰 **100% Free Tier**
Runs entirely on free services:
- Pinecone Serverless (Free)
- Groq API (Free)
- Google BigQuery (Free public dataset)
- Local embeddings (No API costs)

---

## 🎬 Demo

> **Watch the 59-second demo video** showcasing PatentGuard's RAG pipeline in action across three distinct risk levels!

PatentGuard has been tested with real invention ideas to demonstrate its semantic search capabilities. Below are three actual examples that show how the system identifies patent conflicts with different risk levels:

### 🟢 Low Risk Example: Portable Guitar Amplifier

**Input:**
```
A portable guitar amplifier that is foldable and fits inside a backpack. 
It uses a unique hinge mechanism to collapse the speaker cabinet for travel. 
It includes a built-in rechargeable battery and a digital tuner, allowing 
street musicians to play electric guitar anywhere without plugging into a 
wall outlet.
```

**Why Low Risk?**
- Novel hinge mechanism for foldability
- Unique combination of portability features
- Specific use case (backpack-portable for street musicians)
- Minimal overlap with existing amplifier patents

---

### 🟡 Medium Risk Example: Smart Flower Pot

**Input:**
```
A smart flower pot for indoor plants that automatically waters itself. 
It uses a soil moisture sensor to detect when the plant is dry and releases 
water from a built-in reservoir. It connects to a mobile app via Bluetooth 
to send notifications when the water tank needs refilling.
```

**Why Medium Risk?**
- Automatic watering systems exist in prior art
- IoT plant monitoring is an active patent area
- Differentiable through specific sensor integration and app features
- Novel combination of moisture sensing + mobile notifications

---

### 🔴 High Risk Example: Smart Seat Advertising System

**Input:**
```
To propose a new value for a seat, a seat system which can make notification 
of advertising information fit for an occupant seated on the seat with a 
sensor included therein is provided. The seat system includes a sensor 
configured to detect an occupant seated on the seat and an output device 
that notifies the occupant of the advertising information based on the 
detection result.
```

**Why High Risk?**
- Strong overlap with existing IoT seat sensor patents
- Targeted advertising systems are heavily patented
- Sensor-based occupant detection is common in prior art
- Limited novel differentiators identified

---

### 💡 The Technology Behind These Results

PatentGuard uses **semantic understanding** rather than keyword matching:
- Goes beyond exact word matches to understand invention concepts
- Identifies functionally similar patents even with different terminology
- Uses **sentence-transformers** for 384-dimensional vector embeddings
- **Groq's Llama 3.3 70B** analyzes semantic conflicts and provides expert-level risk assessment

### Try It Yourself!
The UI includes **interactive example queries** covering various domains:
- 📱 Smart Home & IoT
- 🏥 Health Wearables
- 🌱 Smart Agriculture
- 🔐 Blockchain Security
- 🎵 Consumer Electronics
- 🌿 Indoor Gardening

---

## 🚀 Tech Stack (100% Free Tier)

<table>
<tr>
<td width="50%">

### Frontend
- ⚛️ **React 19** - Latest React features
- ⚡ **Vite** - Lightning-fast dev server
- 🎨 **Tailwind CSS** - Modern styling
- 📱 **Responsive Design** - Mobile-friendly

</td>
<td width="50%">
---

## 🚀 Quick Start

> **⏱️ Setup Time:** 10-15 minutes | **💰 Cost:** $0 (completely free)

### 📋 Prerequisites

<table>
<tr>
<td width="33%">

**🐍 Python**
```bash
Python 3.11+
pip (package manager)
```
[Download Python](https://www.python.org/)

</td>
<td width="33%">

**📦 Node.js**
```bash
Node.js 18+
npm (package manager)
```
[Download Node.js](https://nodejs.org/)

</td>
<td width="33%">

**☁️ API Keys (Free)**
- [Pinecone](https://www.pinecone.io/)
- [Groq](https://console.groq.com/)
- [Google Cloud](https://console.cloud.google.com/)

</td>
</tr>
</table>
<tr>
<td width="50%">

### AI & Data
- 🧠 **Groq API** - Llama 3.3 70B (Free)
- 🔢 **sentence-transformers** - Local embeddings
- 📊 **Google BigQuery** - Patent dataset
- 🗄️ **Pinecone** - Vector database (Free tier)

</td>
<td width="50%">

### DevOps
- 🔐 **Environment Variables** - Secure config
- 📦 **pip & npm** - Package management
- 🔄 **Hot Reload** - Fast development
- 📚 **API Documentation** - Auto-generated

</td>
</tr>
</table>

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
│   Step 1️⃣: Clone Repository

```bash
git clone https://github.com/Soham-droid-pixel/Patent_Guard.git
cd Patent_Guard
```

### Step 2️⃣: Setup Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install backend dependencies
cd backend
pip install -r requirements.txt
```

### Step 3️⃣: Configure Environment Variables

Create `backend/.env` file with your API keys:

```env
# Pinecone Configuration (Get free key at pinecone.io)
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_INDEX_NAME=patentguard

# Groq API (Get free key at console.groq.com)
GROQ_API_KEY=your_groq_api_key_here

# Google Cloud (Place service-account.json in scripts/ folder)
GOOGLE_APPLICATION_CREDENTIALS=scripts/service-account.json
GOOGLE_CLOUD_PROJECT=your-project-id

# Server Configuration
HOST=0.0.0.0
PORT=8000
```

> 🔒 **Security Note:** Never commit `.env` file to Git! It's already in `.gitignore`

### Step 4️⃣: Setup Google Cloud Authentication

**Option A: Service Account (Recommended)**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable BigQuery API
4. Create a service account with BigQuery User role
5. Download JSON key file
6. Place it at `scripts/service-account.json`

**Option B: gcloud CLI**
```bash
# Install from https://cloud.google.com/sdk/docs/install
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
```

### Step 5️⃣: Ingest Patent Data

```bash
# From project root, with venv activated
cd scripts
python ingest_patents.py
```

**What this does:**
- ✅ Connects to BigQuery public patent dataset
- ✅ Fetches 50 recent US patents
- ✅ Generates embeddings (384-dimensional vectors)
---

## 🎯 How to Use

### 1. Open PatentGuard
Navigate to `http://localhost:5173` in your browser

### 2. Choose Input Method

**Option A: Use Example Queries** (Recommended for first-time users)
---

## 🏗️ System Architecture

### High-Level Flow

```
┌─────────────┐
│   User UI   │
│  (React 19) │
└──────┬──────┘
       │ 1. Invention Description
       ↓
┌──────────────────────────────────────────────────────────┐
---

## 🔌 API Reference

### Base URL
```
http://localhost:8000
```

### Endpoints

#### 📝 Analyze Invention

**POST** `/api/analyze`

Analyzes an invention idea against prior art patents.

**Request Body:**
```json
{
  "invention_idea": "A smart water bottle that tracks hydration levels and reminds users to drink water"
}
```

**Response:** (200 OK)
```json
{
  "risk_level": "High",
  "analysis": "Based on the retrieved patents, this invention poses a HIGH risk...",
  "conflicting_patents": [
    "US-2023-0001234-A1",
    "US-2023-0005678-A1",
    "US-2023-0009012-A1"
  ],
  "recommendations": "Given the high risk level, it is recommended to consult with a patent attorney...",
  "retrieved_patents": [
    {
      "id": "US-2023-0001234-A1",
      "score": 0.892,
      "metadata": {
        "publication_number": "US-2023-0001234-A1",
        "title": "Smart Hydration Tracking Device",
        "abstract": "A portable water bottle equipped with sensors...",
        "publication_date": "20230115"
---

## 🔧 Configuration & Customization

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `PINECONE_API_KEY` | Your Pinecone API key | - | ✅ |
| `PINECONE_INDEX_NAME` | Pinecone index name | `patentguard` | ✅ |
| `GROQ_API_KEY` | Your Groq API key | - | ✅ |
| `GROQ_MODEL` | LLM model to use | `llama-3.3-70b-versatile` | ❌ |
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to service account JSON | - | ✅ |
| `GOOGLE_CLOUD_PROJECT` | GCP project ID | - | ✅ |
| `EMBEDDING_MODEL_NAME` | HuggingFace model | `sentence-transformers/all-MiniLM-L6-v2` | ❌ |
| `EMBEDDING_DIMENSION` | Vector dimensions | `384` | ❌ |
| `HOST` | Backend host | `0.0.0.0` | ❌ |
| `PORT` | Backend port | `8000` | ❌ |
---

## 🐛 Troubleshooting

### Common Issues

<details>
<summary><b>Backend won't start</b></summary>

**Symptoms:** Import errors, module not found

**Solutions:**
```bash
# Make sure venv is activated
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Reinstall dependencies
cd backend
pip install -r requirements.txt
```
</details>

<details>
<summary><b>"No similar patents found" error</b></summary>

**Cause:** Pinecone index is empty

**Solution:**
```bash
# Run ingestion script
cd scripts
python ingest_patents.py
```
</details>

<details>
<summary><b>BigQuery authentication fails</b></summary>

**Check:**
1. Service account JSON is in correct location (`scripts/service-account.json`)
2. Path in `.env` is correct: `GOOGLE_APPLICATION_CREDENTIALS=scripts/service-account.json`
3. Service account has BigQuery User role
4. BigQuery API is enabled in GCP

**Test connection:**
```bash
cd scripts
python test_bigquery.py
```
</details>

<details>
<summary><b>Frontend shows raw JSON</b></summary>

**Solution:** This was fixed in v2.0. Make sure you have latest code:
```bash
git pull origin main
```

If issue persists, clear browser cache (Ctrl + Shift + R)
</details>

<details>
<summary><b>Slow query times (>20 seconds)</b></summary>

**Possible causes:**
- Groq API rate limits (wait 1 minute)
- Poor network connection
- Large number of results being processed

**Normal:** 5-15 seconds per query
</details>

### Getting Help

- 📖 Check [TESTING_EXAMPLES.md](TESTING_EXAMPLES.md)
- 🔧 Review [SETUP_GUIDE.md](SETUP_GUIDE.md)
- 💬 [Open an issue](https://github.com/Soham-droid-pixel/Patent_Guard/issues)
- 📧 Contact: [Your Email]

---

## 📊 Project Stats

- **Lines of Code:** ~3,000+
- **Languages:** Python, JavaScript, CSS
- **Components:** 12+ modular services
- **API Endpoints:** 2
- **Dependencies:** 70+ packages
- **Setup Time:** 10-15 minutes
- **Query Time:** 5-15 seconds

---

## 🗺️ Roadmap

### Q1 2025 ✅
- [x] MVP launch
- [x] BigQuery integration
- [x] Pinecone vector search
- [x] Groq AI analysis
- [x] React frontend
- [x] JSON output fixes

### Q2 2025 🔄
- [ ] User authentication
- [ ] Saved searches
- [ ] PDF export
- [ ] Mobile responsive improvements
- [ ] International patent support

### Q3 2025 📅
- [ ] Patent visualization
- [ ] Advanced search filters
- [ ] API rate limiting
- [ ] Docker deployment
- [ ] CI/CD pipeline

### Q4 2025 🎯
- [ ] Mobile app
- [ ] Enterprise features
- [ ] Patent attorney network
- [ ] Machine learning improvements

---

## 📄 License

**MIT License**

Copyright (c) 2024 Soham (PatentGuard)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

**Free to use, modify, and distribute!** 🎉

---

## 🙏 Acknowledgments

### Technologies

- [Google BigQuery](https://cloud.google.com/bigquery) - Public patent dataset access
- [Pinecone](https://www.pinecone.io/) - Lightning-fast vector database
- [Groq](https://groq.com/) - Ultra-fast LLM inference
- [HuggingFace](https://huggingface.co/) - sentence-transformers models
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [React](https://react.dev/) - UI library
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS

### Inspiration

Built to democratize patent search and make innovation more accessible to everyone, everywhere. 🌍

### Special Thanks

- Patent examiners and attorneys who inspired this project
- Open source community for amazing tools
- Early testers and contributors
- You, for checking out this project! ⭐

---

## 📞 Contact & Support

<div align="center">

### 💬 Get in Touch

**Developer:** Soham  
**GitHub:** [@Soham-droid-pixel](https://github.com/Soham-droid-pixel)  
**Project:** [Patent_Guard](https://github.com/Soham-droid-pixel/Patent_Guard)

---

### ⭐ Support This Project

If you find PatentGuard useful, please consider:

- ⭐ **Star this repository** on GitHub
- 🐛 **Report bugs** or suggest features
- 💻 **Contribute code** via pull requests
- 📢 **Share** with other inventors
- ☕ **Buy me a coffee** (if you'd like!)

---

### 📈 Project Status

![GitHub last commit](https://img.shields.io/github/last-commit/Soham-droid-pixel/Patent_Guard)
![GitHub issues](https://img.shields.io/github/issues/Soham-droid-pixel/Patent_Guard)
![GitHub stars](https://img.shields.io/github/stars/Soham-droid-pixel/Patent_Guard)
![GitHub forks](https://img.shields.io/github/forks/Soham-droid-pixel/Patent_Guard)

---

**Built with ❤️ for inventors, innovators, and entrepreneurs worldwide**

*Protect your ideas. Power your innovation. PatentGuard has your back.* 🛡️

</div>

# Filter by country
query = """
WHERE country_code = 'US'  # US patents only
```

### Adjusting Search Parameters

Edit `backend/app/api/routes.py`:

```python
# Return more similar patents
results = pinecone_service.query_similar(query_embedding, top_k=10)  # Default: 5

# Adjust similarity threshold
if match['score'] > 0.8:  # Default: 0.7
    patents.append(match)
```

---

## 📝 Development Notes

### Technical Specifications

- **Embedding Model**: `sentence-transformers/all-MiniLM-L6-v2`
  - Dimensions: 384
  - Model size: ~80MB (local, no API calls)
  - Speed: ~20ms per embedding

- **Vector Database**: Pinecone Serverless
  - Metric: Cosine similarity
  - Free tier: 100K queries/month
  - Index size: Unlimited storage

- **LLM**: Groq (Llama 3.3 70B)
  - Speed: ~500 tokens/second
  - Context: 8,192 tokens
  - Free tier: 30 requests/minute

- **Patent Data**: Google BigQuery
  - Dataset: `patents-public-data.patents.publications`
  - Records: Millions of patents
  - Free tier: 1 TB queries/month

### Performance Benchmarks

| Operation | Time | Notes |
|-----------|------|-------|
| Generate embedding | ~20ms | Local processing |
| Pinecone query | ~100-200ms | Network latency |
| Groq LLM analysis | 3-10s | Depends on output length |
| **Total query time** | **5-15s** | End-to-end |

### Code Quality

- ✅ Type hints throughout Python code
- ✅ Async/await for concurrent operations
- ✅ Error handling with detailed logging
- ✅ Pydantic models for data validation
- ✅ ESLint for frontend code quality
- ✅ Environment-based configuration

---

## 🤝 Contributing

We welcome contributions from developers worldwide! 🌍

### Ways to Contribute

1. **🐛 Bug Reports**: Found an issue? [Open an issue](https://github.com/Soham-droid-pixel/Patent_Guard/issues)
2. **✨ Feature Requests**: Have an idea? We'd love to hear it!
3. **💻 Code Contributions**: Submit a pull request
4. **📖 Documentation**: Help improve our docs
5. **🌐 Translations**: Add support for other languages

### Development Setup

```bash
# Fork the repository
git clone https://github.com/YOUR_USERNAME/Patent_Guard.git
cd Patent_Guard

# Create a branch
git checkout -b feature/your-feature-name

# Make your changes
# Test thoroughly

# Commit and push
git add .
git commit -m "Add: your feature description"
git push origin feature/your-feature-name

# Open a Pull Request
```

### Improvement Ideas

**🚀 High Priority:**
- [ ] User authentication & saved searches
- [ ] Export results to PDF
- [ ] Email notifications for new similar patents
- [ ] Patent similarity visualization graphs
- [ ] Batch analysis (multiple inventions at once)

**💡 Nice to Have:**
- [ ] Support for international patents (EP, JP, CN)
- [ ] Patent image analysis
- [ ] Citation network visualization
- [ ] Historical trend analysis
- [ ] Patent attorney integration
- [ ] Mobile app (React Native)

**🎨 UI/UX Enhancements:**
- [ ] Dark mode
- [ ] Advanced search filters
- [ ] Patent comparison tool
- [ ] Interactive charts and graphs
- [ ] Keyboard shortcuts

**⚙️ Technical Improvements:**
- [ ] Redis caching for common queries
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Automated testing suite
- [ ] Performance monitoring
**Response:** (200 OK)
```json
{
  "status": "healthy",
  "service": "PatentGuard API"
}
```

### Interactive API Docs

Visit `http://localhost:8000/docs` for:
- 📖 Complete API documentation
- 🧪 Interactive request testing
- 📋 Request/response schemas
- 🔍 Model definitions

### Rate Limits

**Free Tier Limits:**
- Groq: 30 requests/minute
- Pinecone: 100,000 queries/month
- BigQuery: 1 TB/month (public dataset is free)

No rate limiting on PatentGuard itself.                                                         │
└──────────────────────────────────────────────────────────┘
       │ 5. Structured Results
       ↓
┌─────────────┐
│  Results UI │
│ (Color-coded)│
└─────────────┘
```

### Data Pipeline

```
┌──────────────────┐
│  Google BigQuery │ ← Patent data source
│ (Public Dataset) │   (Millions of US patents)
└────────┬─────────┘
         │
         │ scripts/ingest_patents.py
         ↓
┌──────────────────┐
│ Embedding Service│
│ Local Processing │
└────────┬─────────┘
         │
         │ 384-dim vectors
         ↓
┌──────────────────┐
│    Pinecone      │ ← Vector database
│ (50+ patents)    │   (Searchable index)
└──────────────────┘
```

### Key Components

#### 🎨 Frontend (React)
- **SearchInput.jsx**: User input with example queries
- **ResultsDisplay.jsx**: Color-coded results rendering
- **client.js**: API communication layer

#### ⚙️ Backend (FastAPI)
- **routes.py**: API endpoints (`/analyze`, `/health`)
- **config.py**: Environment configuration
- **prompts.py**: LLM system prompts

#### 🤖 AI Services
- **embedding_svc.py**: Text → Vector conversion
- **pinecone_svc.py**: Vector storage & search
- **bigquery_svc.py**: Patent data fetching
- **llm_svc.py**: AI analysis with JSON cleaning

#### 📊 Recent Improvements (v2.0)
- ✅ **JSON Cleaning**: Strips markdown artifacts from LLM
- ✅ **Enhanced Prompts**: Forces valid JSON output
- ✅ **Frontend Parsing**: Safely handles various formats
- ✅ **Better Logging**: Tracks full analysis pipeline
- ✅ **Risk Consistency**: Accurate risk level extraction
<table>
<tr>
<td width="33%">

**📊 Risk Level**
- 🔴 High
- 🟡 Medium  
- 🟢 Low

Color-coded banner

</td>
<td width="33%">

**📋 Analysis**
- Conflict details
- Key patent overlaps
- Novel aspects
- Expert insights

</td>
<td width="33%">

**💡 Recommendations**
- Action items
- Differentiation tips
- Next steps
- Attorney consultation

</td>
</tr>
</table>

### 5. Review Similar Patents
- See 3-5 most similar patents
- View similarity scores (0-100%)
- Read titles and abstracts
- Check publication numbers

---

## 🎨 Screenshots

<table>
<tr>
<td width="50%">

### Home Screen
Clean, professional interface with example queries

</td>
<td width="50%">

### Results View
Color-coded risk assessment with detailed analysis

</td>
</tr>
<tr>
<td width="50%">

### Patent List
Similar patents with similarity scores

</td>
<td width="50%">

### Recommendations
Actionable advice for inventors

</td>
</tr>
</table>
✓ Fetched 50 patents

[3/4] Generating embeddings...
✓ Generated 50 embeddings

[4/4] Uploading to Pinecone...
✓ All vectors uploaded

INGESTION COMPLETE! Total patents: 50
```

### Step 6️⃣: Start Backend Server

```bash
cd backend
python -m uvicorn app.main:app --reload
```

✅ Backend running at: `http://localhost:8000`  
📚 API Docs at: `http://localhost:8000/docs`

### Step 7️⃣: Start Frontend

```bash
# In a NEW terminal
cd frontend
npm install
npm run dev
```

✅ Frontend running at: `http://localhost:5173`

### Step 8️⃣: Test It Out! 🎉

1. Open browser to `http://localhost:5173`
2. Click one of the **4 example queries**
3. Click **"Analyze for Prior Art"**
4. Get instant results in 5-15 seconds!

---

## 📚 Detailed Setup Guides

For more detailed instructions, see:
- [SETUP_GUIDE.md](SETUP_GUIDE.md) - Complete setup walkthrough
- [BIGQUERY_SETUP.md](BIGQUERY_SETUP.md) - BigQuery configuration
- [TESTING_EXAMPLES.md](TESTING_EXAMPLES.md) - Testing examples
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Quick command reference
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

---

## 🚀 Current Status & Vision

### Where PatentGuard Stands Now

This is an **MVP (Minimum Viable Product)** and **Proof of Concept** demonstrating the power of AI in patent prior art search. The system currently:

- ✅ Successfully ingested **50 curated US patents** into the vector space
- ✅ Semantic search that catches similarities traditional keyword searches miss
- ✅ Professional-grade risk analysis powered by Groq's Llama 3.3 70B
- ✅ Real-time results in 5-15 seconds
- ✅ 100% free to use with zero API costs on free tiers

### The Vision

PatentGuard proves that **AI can be more than just a chatbot**—it can be a sophisticated **Engineering Shield for creators and innovators**. The goal is to:

- 🎯 Democratize innovation by removing financial barriers to patent searches
- 🌍 Make professional-grade IP analysis accessible to independent inventors worldwide
- 🚀 Scale to millions of patents across multiple countries and patent offices
- 💡 Help creators make informed decisions before investing in product development
- 🛡️ Empower startups and small businesses to protect their innovations

### Why This Matters

Patent searches shouldn't be a luxury reserved for well-funded companies. Every inventor deserves to know if their idea conflicts with existing IP—**without spending thousands of dollars**. PatentGuard is a step toward that future.

### Future Roadmap

- 📈 Scale ingestion to **millions of patents** from multiple countries
- 🌐 Add support for **international patent offices** (EPO, JPO, WIPO)
- 📊 Implement **advanced visualization** of patent landscapes
- 🔔 Add **patent monitoring** for specific technology domains
- 💾 Build **query caching** for faster repeated searches
- 🔐 Add **user authentication** and search history
- 📱 Develop **mobile app** for on-the-go patent checking
- 🤖 Fine-tune models specifically for patent domain understanding

---

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

---

## 👨‍💻 About the Developer

Built by **Soham** - Computer Engineering student passionate about building impactful, production-grade systems using AI and modern web technologies.

**Currently seeking:** Software Engineering or Data Science Internships (starting June 2026) where I can contribute to solving real-world problems with technology.

**Tech Focus:** React, FastAPI, AI/ML, RAG Systems, Full-Stack Development

Connect on [LinkedIn](https://www.linkedin.com/in/soham-droid-pixel) | View on [GitHub](https://github.com/Soham-droid-pixel/Patent_Guard)

---

## 🙏 Acknowledgments

- Google BigQuery for public patent dataset
- Pinecone for vector database free tier
- Groq for fast LLM inference
- HuggingFace for sentence-transformers

---

**Built with ❤️ for inventors and innovators worldwide**
