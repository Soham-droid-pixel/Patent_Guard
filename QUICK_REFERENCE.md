# 🚀 PatentGuard - Quick Testing Reference

## Start Commands

```bash
# Terminal 1 - Backend
cd backend
python -m uvicorn app.main:app --reload

# Terminal 2 - Frontend  
cd frontend
npm run dev

# Open: http://localhost:5173
```

---

## 📝 Copy-Paste Test Queries

### 1️⃣ Smart Home IoT (HIGH RISK Expected)
```
A voice-activated smart home energy management system that uses artificial intelligence to optimize energy consumption. The system integrates with smart appliances, learns usage patterns, and automatically adjusts power usage to reduce electricity costs while maintaining comfort levels.
```

### 2️⃣ Health Wearable (HIGH RISK Expected)
```
A wearable health monitoring device that continuously tracks vital signs including heart rate, blood pressure, and temperature. Uses machine learning algorithms to detect health anomalies and sends immediate alerts to users and healthcare providers through a mobile application.
```

### 3️⃣ Smart Agriculture (MEDIUM RISK Expected)
```
An intelligent automated plant care system featuring soil moisture sensors, automated watering mechanisms, and smartphone connectivity. The system learns optimal watering schedules and adjusts based on environmental conditions like temperature and humidity.
```

### 4️⃣ Blockchain Security (HIGH RISK Expected)
```
A blockchain-based secure data storage system that provides end-to-end encryption for sensitive information. The platform enables decentralized data sharing across multiple platforms while protecting user privacy and ensuring data integrity.
```

### 5️⃣ Novel Concept (LOW-MEDIUM RISK Expected)
```
A self-cleaning solar panel system using microscopic vibrating surfaces powered by piezoelectric materials that generate cleaning energy from rain droplets, eliminating the need for manual maintenance or external power sources.
```

---

## ✅ Quick Verification Checklist

- [ ] Backend running on port 8000
- [ ] Frontend running on port 5173
- [ ] See 4 example buttons on homepage
- [ ] Click example → textarea fills
- [ ] Click "Analyze for Prior Art"
- [ ] Loading spinner shows
- [ ] Results appear in 5-15 seconds
- [ ] Risk level banner displays
- [ ] Analysis text is readable
- [ ] See 3-5 patent numbers (US-XXXX...)
- [ ] Backend logs show "BigQuery initialized"
- [ ] Backend logs show "Connected to index: patentguard"

---

## 🎯 Expected Results

### What Success Looks Like:

1. **Risk Level Banner** (colored):
   - 🔴 HIGH = Red background
   - 🟡 MEDIUM = Yellow background  
   - 🟢 LOW = Green background

2. **Conflict Analysis** section with detailed AI analysis

3. **Recommendations** section with actionable advice

4. **Patent List** showing:
   - Patent numbers: `US-2025328664-A1`
   - Patent titles from BigQuery
   - 3-5 most similar patents

---

## 🐛 Quick Fixes

### No Patents Found?
```bash
cd scripts
python ingest_patents.py
# Adds 50 patents from BigQuery to Pinecone
```

### Backend Error?
```bash
.\venv\Scripts\Activate.ps1
cd backend
pip install -r requirements.txt
```

### Check Services?
```bash
# Test BigQuery
cd scripts
python test_bigquery.py

# Should show: ✅ BigQuery is working correctly!
```

---

## 📊 System Architecture (For Understanding)

```
User Input (Frontend)
    ↓
FastAPI Backend (Port 8000)
    ↓
Generate Embedding (Sentence Transformers)
    ↓
Search Pinecone (Vector DB) → 50 patents from BigQuery
    ↓
Groq AI Analysis (Llama 3.3 70B)
    ↓
Results (Frontend Display)
```

---

## 🔢 Key Metrics

- **Query Time**: 5-15 seconds
- **Patents in DB**: 50 from BigQuery
- **Embedding Model**: all-MiniLM-L6-v2 (384 dimensions)
- **AI Model**: Llama 3.3 70B via Groq
- **Vector DB**: Pinecone serverless

---

## 💡 Understanding Results

### HIGH RISK ⚠️
- Multiple existing patents in this area
- Significant overlap with prior art
- **Action**: Consult patent attorney, consider pivoting

### MEDIUM RISK ⚡
- Some similar patents exist
- May be differentiable with proper claims
- **Action**: Document unique aspects, research deeper

### LOW RISK ✅
- Few or no direct conflicts
- Novel approach or combination
- **Action**: Proceed with development, consider filing patent

---

## 🎓 Pro Tips

1. **More Details = Better Results**: Longer, more detailed descriptions get better matches
2. **Try Multiple Variations**: Rephrase your invention in different ways
3. **Check Patent Numbers**: Click through to verify actual patent content
4. **Use Technical Terms**: AI understands domain-specific terminology
5. **Test Edge Cases**: Try very specific vs very broad descriptions

---

## 📁 Important Files

- `backend/.env` - API keys and config
- `scripts/service-account.json` - BigQuery credentials  
- `scripts/ingest_patents.py` - Add more patents
- `backend/app/main.py` - FastAPI server
- `frontend/src/App.jsx` - React frontend

---

## 🌐 URLs

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- API Health: http://localhost:8000/

---

## 🎉 Success Message

If you see this in backend logs:
```
✓ BigQuery initialized with service account
  Project: strange-cosmos-451704-p5
Connected to index: patentguard
Found X similar patents
Generated analysis from Groq
```

**YOU'RE ALL SET! 🚀**

---

## 📞 Next Steps

1. ✅ Test all 5 examples
2. ✅ Verify different risk levels
3. ✅ Check patent numbers are real (US-XXXX format)
4. ✅ Read through AI analysis quality
5. ✅ Try your own invention ideas!

**Your BigQuery → Pinecone → AI pipeline is LIVE!** 🎊
