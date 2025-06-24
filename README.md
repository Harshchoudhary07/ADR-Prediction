# 🧠 ADR Prediction System

An AI-based web application that predicts the **risk of Adverse Drug Reactions (ADRs)** before prescribing a drug — using patient medical history, symptoms, and available drug interaction data.

## 🚀 Features

- 🧬 Predicts ADR risk using ML models
- 🏥 Patient-friendly and doctor-friendly UI
- 💊 Suggests safer drug alternatives
- 🔐 Data privacy-first architecture
- 📊 Downloadable risk reports

---

## 🔎 User Journey

1. **Login / Signup**
2. **Enter Medical Profile** — age, gender, history, current medications
3. **Input Symptoms** — manually or via checklist
4. **View ADR Risk Report** — for entered or suggested drugs
5. **Download or Share Summary** with physician
6. *(Optional)* View history, track reactions, or update profile

---

## 🛠️ Tech Stack

| Layer        | Tech                           |
|--------------|--------------------------------|
| Frontend     | HTML, CSS, JavaScript          |
| Backend      | Python, Django                 |
| ML/AI        | scikit-learn, pandas, numpy    |
| Database     | SQLite / PostgreSQL (configurable) |
| Deployment   | (Optional: Docker, Render, etc.) |

---



---

## ⚙️ Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/Harshchoudhary07/ADR-Prediction.git
cd ADR-Prediction

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start the server
python manage.py runserver

