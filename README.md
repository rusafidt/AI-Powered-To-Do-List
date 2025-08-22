# 📝 AI-Powered To-Do List

An intelligent To-Do List app that uses **spaCy NLP** to automatically tag tasks into categories like **Shopping, Work, Health, Personal, or Other**.

---

## 🚀 Features
-> Auto-tag tasks based on keywords (lemmatized with spaCy)
-> Categories: Shopping, Work, Health, Personal, Other
-> Simple and lightweight NLP pipeline
-> Extendable (you can add more categories & keywords easily)

---

## 📦 Setup

### 1. Install dependecies
```bash
pip install -U spacy
python -m spacy download en_core_web_sm
```

--- 

## ⚠️ Issues & Fixes

❌ Error: ValueError: numpy.dtype size changed, may indicate binary incompatibility
This happens when numpy, h5py, and spaCy versions don’t match.

✅ Fix
Run these commands inside your environment:
```bash
pip uninstall spacy thinc h5py numpy -y
pip install -U spacy
python -m spacy download en_core_web_sm
```

---

## 🔮 Future Improvements

-> Support multiple category matches per task
-> Add ML-based classifier for smarter tagging
-> Integrate with a simple Flask/Streamlit web app