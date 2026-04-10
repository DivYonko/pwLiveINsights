# 📡 LivePulse — YouTube Live Chat Analytics

> ⚠️ Note: Large ML models are hosted externally. See "Model Weights / Trained Data" section below.

Real-time sentiment and topic analysis for YouTube live streams. Scrape live chat, classify messages using a Hinglish-aware ML ensemble, and visualize everything on an auto-refreshing dashboard.

---

## ⚡ Quick Start

```bash
git clone <your-repo-url>
cd pwLiveINsights

pip install -r requirements.txt

# Download trained model (see section below)
# python download_data.py  (optional if you implement it)

streamlit run frontend/streamlit_app.py
```

---

## 🚀 Features

* Real-time chat scraping via pytchat
* Sentiment classification (Positive / Neutral / Negative) using a 3-model ensemble

  * Fine-tuned MuRIL (Hinglish-aware, highest weight)
  * XLM-RoBERTa (multilingual Twitter model)
  * Multilingual sentiment model
* Topic classification (Appreciation / Question / Promo / Spam / MCQ Answer / General)

  * Keyword fast-path for speed
  * Zero-shot BART-large-MNLI fallback
* Interactive Streamlit dashboard with live auto-refresh
* Start/stop scraper directly from the UI — no terminal needed
* Redis-backed message queue (configurable cap)
* CSV export for all charts and feeds
* FastAPI REST endpoints for external consumers

---

## 🧠 System Architecture

```
YouTube Live Chat
        ↓
    pytchat scraper
        ↓
 ML Processing (Sentiment + Topic)
        ↓
      Redis Queue
        ↓
 FastAPI + Streamlit Dashboard
```

---

## 📁 Project Structure

```
├── backend/
│   ├── config.py
│   ├── scraper.py
│   └── main.py
├── frontend/
│   └── streamlit_app.py
├── ml/
│   ├── sentiment_model.py
│   ├── topic_model.py
│   └── train_muril.py
├── new_trained_data/        # ❌ Not included in repo
│   └── muril-sentimix/
├── Redis-x64-5.0.14.1/      # ❌ Ignored (local use only)
└── requirements.txt
```

---

## 📦 Model Weights / Trained Data

The fine-tuned MuRIL model is not included in this repository due to GitHub file size limits.

👉 **Download from Google Drive:** <PASTE YOUR DRIVE LINK HERE>

### 📁 Setup Instructions

1. Download the file
2. Extract it
3. Place it inside:

```
new_trained_data/muril-sentimix/
```

### ✅ Final Structure

```
new_trained_data/
└── muril-sentimix/
    ├── config.json
    ├── pytorch_model.bin
    └── ...
```

⚠️ Ensure the folder structure matches exactly, otherwise the model will fail to load.

---

## ⚙️ Requirements

* Python 3.11
* Redis 5.0
* GPU optional (CUDA supported, falls back to CPU automatically)

---

## 🛠️ Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Redis

**Windows (included):**

```bash
Redis-x64-5.0.14.1/redis-server.exe
```

**Linux/Mac:**

```bash
redis-server
```

### 3. Run the dashboard

```bash
streamlit run frontend/streamlit_app.py
```

The scraper can be fully controlled from the dashboard sidebar.

---

## 📊 Usage

1. Open the dashboard at `http://localhost:8501`
2. Paste a YouTube live video ID or URL in the **Scraper Control** section
3. Click **▶ Start** to begin scraping
4. View real-time sentiment and topic analytics
5. Use filters to explore chat data
6. Click **⏹ Stop** to end scraping

---

## ⚙️ Configuration

All config is in `backend/config.py` and supports environment variables:

| Variable   | Default     | Description      |
| ---------- | ----------- | ---------------- |
| VIDEO_ID   | eFSK2-QRB0A | YouTube video ID |
| REDIS_HOST | localhost   | Redis host       |
| REDIS_PORT | 6379        | Redis port       |
| REDIS_DB   | 0           | Redis DB index   |

Override example:

```bash
VIDEO_ID=abc123 streamlit run frontend/streamlit_app.py
```

---

## 🌐 REST API

Start the API server:

```bash
uvicorn backend.main:app --reload --port 8000
```

| Endpoint               | Description                  |
| ---------------------- | ---------------------------- |
| GET /health            | Redis connectivity check     |
| GET /get_messages      | Last N raw messages          |
| GET /sentiment_trend   | Time-series sentiment data   |
| GET /sentiment_summary | Aggregate sentiment stats    |
| GET /topic_stats       | Topic-wise counts            |
| GET /live_stats        | Combined real-time analytics |

---

## 🧩 Topic Categories

| Topic        | Description                         |
| ------------ | ----------------------------------- |
| Appreciation | Praise, encouragement               |
| Question     | Doubts and queries                  |
| Promo        | Self-promotion, links               |
| Spam         | Repetitive or irrelevant messages   |
| MCQ Answer   | Short answers like "a", "bb", "ccc" |
| General      | Everything else                     |

---

## 🤖 Sentiment Model Details

The ensemble combines three models with weighted averaging:

| Model              | Weight | Notes                          |
| ------------------ | ------ | ------------------------------ |
| MuRIL (fine-tuned) | 0.55   | Hinglish SentiMix dataset      |
| XLM-RoBERTa        | 0.20   | Twitter multilingual sentiment |
| Multilingual model | 0.25   | General fallback               |

A keyword fast-path is used before the ensemble to improve speed for common Hinglish expressions.

---

## 📚 References

* MuRIL — https://huggingface.co/google/muril-base-cased
* XLM-RoBERTa Sentiment — https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment
* BART-large-MNLI — https://huggingface.co/facebook/bart-large-mnli
* pytchat — https://github.com/taizan-hokuto/pytchat
* SentiMix Dataset — https://ritual.uh.edu/semeval-2020-task-9/

---
