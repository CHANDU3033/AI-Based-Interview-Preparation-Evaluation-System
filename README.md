# 🎯 AI-Based Interview Preparation & Evaluation System

> **Final Year B.Tech Project — AI & Data Science**

A full-stack AI-powered mock interview platform that conducts personalized interviews, evaluates answers using NLP, and provides detailed performance reports with personalized recommendations.

---

## 🚀 Features

| Module | Description |
|---|---|
| 🔐 Authentication | Register, Login, JWT-secured sessions |
| 🎯 Interview Setup | Select role, difficulty, question count |
| 🤖 AI Questions | Groq LLM generates dynamic questions |
| 📝 Mock Interview | Answer questions with real-time timer |
| 🧠 AI Evaluation | NLP-based scoring: relevance, accuracy, completeness |
| 📊 Performance Report | Per-question breakdown + overall score |
| 📈 Dashboard | Score progression charts, weak/strong topics |
| 💡 Recommendations | Personalized study plan based on weak areas |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React 18 + Vite + Tailwind CSS + Recharts |
| Backend | Python + FastAPI + SQLAlchemy |
| Database | SQLite (dev) / PostgreSQL (prod) |
| AI/LLM | Groq API (llama-3.1-8b-instant) |
| NLP | scikit-learn TF-IDF similarity |
| Auth | JWT (python-jose + bcrypt) |
| Speech | Whisper (Phase 2) |

---

## 📁 Project Structure

```
ai-interview-system/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI entry point
│   │   ├── config.py            # Settings from .env
│   │   ├── database.py          # SQLAlchemy setup
│   │   ├── models/              # DB models
│   │   ├── schemas/             # Pydantic schemas
│   │   ├── routers/             # API route handlers
│   │   ├── ai/                  # Groq + NLP engines
│   │   ├── data/                # Question bank (300+ questions)
│   │   └── utils/               # Auth helpers
│   ├── seed_data.py             # Seed DB with questions
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── pages/               # Login, Register, Dashboard, Interview...
│   │   ├── components/          # Reusable UI components
│   │   ├── services/            # API service layer
│   │   └── contexts/            # Auth context
│   └── package.json
├── data/
│   └── questions.csv            # Question bank export
└── notebooks/
    └── evaluation_testing.ipynb
```

---

## ⚡ Quick Start

### 1. Clone & Setup

```bash
git clone <repo-url>
cd ai-interview-system
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Configure environment
copy .env.example .env
# Edit .env and add your GROQ_API_KEY

# Seed the database (job roles + 300+ questions)
python seed_data.py

# Start backend
uvicorn app.main:app --reload
```

Backend runs at: http://localhost:8000
API docs: http://localhost:8000/docs

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start frontend
npm run dev
```

Frontend runs at: http://localhost:5173

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | JWT signing secret (make it long & random) |
| `DATABASE_URL` | `sqlite:///./ai_interview.db` (dev) or PostgreSQL URL (prod) |
| `GROQ_API_KEY` | Free API key from [console.groq.com](https://console.groq.com) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry (default: 10080 = 7 days) |

---

## 🗄️ Database Schema

```
users
  └── interviews
        └── answers
              └── evaluations

job_roles
  └── questions
```

---

## 📊 Evaluation Metrics

| Metric | Description |
|---|---|
| Relevance Score | How relevant the answer is to the question |
| Technical Accuracy | Correctness of technical concepts |
| Completeness | Coverage of expected concepts |
| Semantic Similarity | NLP similarity to expected answer |
| Communication | Clarity and structure of response |
| **Overall Score** | Weighted average of all metrics |

> Scores are AI-generated estimates to guide learning, not objective measures of ability.

---

## 🎯 Supported Job Roles

- 🐍 Python Developer
- 📊 Data Analyst
- 🤖 AI/ML Engineer
- 🗃️ SQL Developer
- 💻 Software Developer

---

## 🗺️ Development Roadmap

- [x] Phase 1: Text-based mock interview system
- [x] Phase 1: AI question generation (Groq)
- [x] Phase 1: NLP answer evaluation
- [x] Phase 1: Performance dashboard
- [ ] Phase 2: Voice interview (Whisper STT)
- [ ] Phase 2: Speech analysis (filler words, WPM)
- [ ] Phase 2: Resume-based personalization
- [ ] Phase 2: Advanced recommendation engine

---

## 👨‍💻 Author

**Srikar** — B.Tech AI & Data Science

---

## 📄 License

MIT License — Free to use for academic projects.
