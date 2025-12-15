# PatentGuard Testing Examples

## 🚀 Quick Start

1. **Start Backend**: 
   ```bash
   cd backend
   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Start Frontend**: 
   ```bash
   cd frontend
   npm run dev
   ```

3. **Open Browser**: Navigate to `http://localhost:5173`

---

## 📝 Test Examples

These examples will help you verify that your BigQuery → Pinecone → Groq AI pipeline is working correctly.

### Example 1: Smart Home Energy Management 🏠
**Test Query:**
```
A voice-activated smart home energy management system that uses artificial intelligence to optimize energy consumption. The system integrates with smart appliances, learns usage patterns, and automatically adjusts power usage to reduce electricity costs while maintaining comfort levels.
```

**Expected Results:**
- Should find patents related to smart home systems, energy management, voice control
- Risk level: Likely HIGH or MEDIUM (this is a common patent area)
- Analysis should mention existing patents in smart home automation

---

### Example 2: Health Monitoring Wearable 🏥
**Test Query:**
```
A wearable health monitoring device that continuously tracks vital signs including heart rate, blood pressure, and temperature. Uses machine learning algorithms to detect health anomalies and sends immediate alerts to users and healthcare providers through a mobile application.
```

**Expected Results:**
- Should find patents related to wearable health devices, vital sign monitoring
- Risk level: Likely HIGH (heavily patented area)
- Analysis should identify conflicts with existing health monitoring patents

---

### Example 3: Automated Plant Care System 🌱
**Test Query:**
```
An intelligent automated plant care system featuring soil moisture sensors, automated watering mechanisms, and smartphone connectivity. The system learns optimal watering schedules and adjusts based on environmental conditions like temperature and humidity.
```

**Expected Results:**
- Should find patents related to automated irrigation, IoT sensors
- Risk level: Could be LOW to MEDIUM
- Analysis should discuss smart agriculture patents

---

### Example 4: Data Protection Platform 🔐
**Test Query:**
```
A blockchain-based secure data storage system that provides end-to-end encryption for sensitive information. The platform enables decentralized data sharing across multiple platforms while protecting user privacy and ensuring data integrity.
```

**Expected Results:**
- Should find patents related to data encryption, blockchain, security
- Risk level: Likely HIGH (blockchain patents are common)
- Analysis should mention existing data protection patents

---

### Example 5: Air Quality Monitor 🌬️
**Test Query:**
```
A portable air quality monitoring device that measures indoor pollutants including CO2, volatile organic compounds, and particulate matter. Features real-time data display and sends alerts to users' smartphones when air quality deteriorates below healthy levels.
```

**Expected Results:**
- Should find patents related to air quality sensors, IoT monitoring
- Risk level: Could be MEDIUM to HIGH
- Analysis should identify environmental monitoring patents

---

### Example 6: Novel/Unique Invention (Lower Risk) 💡
**Test Query:**
```
A self-cleaning solar panel system using microscopic vibrating surfaces powered by piezoelectric materials that generate cleaning energy from rain droplets, eliminating the need for manual maintenance or external power sources.
```

**Expected Results:**
- Should find some solar panel or self-cleaning patents
- Risk level: Likely LOW to MEDIUM (more novel concept)
- Analysis should note the uniqueness of the approach

---

## 🔍 What to Verify

### 1. **Backend Connectivity**
- [ ] Backend server starts without errors
- [ ] Can access `http://localhost:8000/docs` (FastAPI docs)
- [ ] Logs show BigQuery connection successful
- [ ] Logs show Pinecone connection successful

### 2. **BigQuery Integration**
- [ ] Backend logs show: "✓ BigQuery initialized with service account"
- [ ] Project ID shown: `strange-cosmos-451704-p5`
- [ ] Patents are being fetched from Google BigQuery

### 3. **Pinecone Vector Search**
- [ ] Backend logs show: "Connected to index: patentguard"
- [ ] When you search, you should see "Found X similar patents"
- [ ] Results should include actual patent numbers (e.g., US-2025328664-A1)

### 4. **Groq AI Analysis**
- [ ] Each search generates a detailed analysis
- [ ] Risk levels are assigned (HIGH, MEDIUM, LOW)
- [ ] Recommendations are provided
- [ ] Analysis mentions specific patent conflicts

### 5. **Frontend Display**
- [ ] Example buttons work and populate the textarea
- [ ] Search button shows "Analyzing with AI..." when loading
- [ ] Results display with proper color coding:
  - 🔴 RED = High Risk
  - 🟡 YELLOW = Medium Risk
  - 🟢 GREEN = Low Risk
- [ ] Patent titles and numbers are shown
- [ ] Analysis text is readable and formatted

---

## 🐛 Troubleshooting

### Backend won't start
```bash
# Make sure you're in venv
cd C:\Users\soham\OneDrive\Desktop\PatentGuard
.\venv\Scripts\Activate.ps1

# Install dependencies
cd backend
pip install -r requirements.txt

# Check .env file exists
cat .env
```

### Frontend won't start
```bash
cd frontend
npm install
npm run dev
```

### "BigQuery not connected" error
- Check `backend/.env` has: `GOOGLE_APPLICATION_CREDENTIALS=scripts/service-account.json`
- Verify `scripts/service-account.json` exists
- Check backend logs for authentication errors

### "Pinecone error" messages
- Check `backend/.env` has valid `PINECONE_API_KEY`
- Verify index name is correct: `patentguard`
- Log into Pinecone dashboard to verify index exists

### "No similar patents found"
- Run the ingestion script again:
  ```bash
  cd scripts
  python ingest_patents.py
  ```
- This will add 50 patents to Pinecone

---

## 📊 Expected Performance

- **Query Time**: 5-15 seconds per search
  - Embedding generation: ~1 second
  - Pinecone vector search: ~1-2 seconds
  - Groq AI analysis: ~3-10 seconds

- **Accuracy**: The system should find relevant patents based on semantic similarity
- **Patents Returned**: Typically 3-5 most similar patents

---

## ✅ Success Indicators

You'll know everything is working when:

1. ✅ You can click an example button
2. ✅ The textarea fills with the example text
3. ✅ Click "Analyze for Prior Art" button
4. ✅ See "Analyzing with AI..." loading state
5. ✅ Get results showing:
   - Risk level with colored banner
   - Detailed conflict analysis
   - Recommendations
   - List of conflicting patents with US patent numbers
   - Patent titles from BigQuery data
6. ✅ Try different examples and get different results
7. ✅ Backend logs show successful queries

---

## 🎓 Understanding the Results

### Risk Levels Explained

- **HIGH Risk** ⚠️: Your invention has significant overlap with existing patents. You should:
  - Consult a patent attorney
  - Consider modifying your approach
  - Be prepared for potential patent conflicts

- **MEDIUM Risk** ⚡: Some similarities exist but may not be blocking. You should:
  - Review the conflicting patents carefully
  - Document how your invention differs
  - Consider patent attorney consultation

- **LOW Risk** ✅: Few or no significant conflicts. You may:
  - Proceed with development
  - Still recommended to do thorough patent search
  - Consider filing a patent application

---

## 🔄 Re-ingesting Data

If you want to fetch fresh patents from BigQuery:

```bash
cd scripts
python ingest_patents.py
```

This will:
- Fetch 50 recent US patents from BigQuery
- Generate embeddings for each patent
- Upload to Pinecone index

You can run this multiple times to add more patents!

---

## 📞 Support

If something isn't working:
1. Check backend logs for error messages
2. Verify all environment variables in `.env`
3. Ensure all services (BigQuery, Pinecone, Groq) have valid API keys
4. Try the test scripts in `scripts/` folder

Happy Testing! 🚀
