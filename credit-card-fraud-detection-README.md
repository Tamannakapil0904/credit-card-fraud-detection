# 💳 Credit Card Fraud Detection API

This project is a machine learning-powered system that detects fraudulent credit card transactions using real-world data. It includes a REST API built with Flask, model training using Logistic Regression, and automated testing with Pytest — everything recruiters love to see in a well-rounded software/project engineer!

---

## 🚀 Features

- ✅ Model training using Logistic Regression
- ✅ Data preprocessing with StandardScaler
- ✅ REST API using Flask
- ✅ Fraud prediction endpoint (`/predict`)
- ✅ Health check endpoint (`/health`)
- ✅ Unit/API testing with `pytest`
- ✅ GitHub-ready structure with modular code

---

## 🧠 Technologies Used

- Python 3.x  
- Pandas, NumPy  
- Scikit-learn  
- Flask  
- Joblib  
- Pytest  
- Git / GitHub

---

## 📂 Project Structure

```
credit-card-fraud-detection/
├── app/
│   ├── app.py           # Flask REST API
│   └── train.py         # Model training script
├── models/
│   ├── fraud_model.pkl  # Trained model
│   └── scaler.pkl       # Data scaler
├── tests/
│   └── test_api.py      # Automated API tests
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 📦 How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Tamannakapil0904/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Train the model

```bash
python app/train.py
```

### 4️⃣ Start the API server

```bash
python app/app.py
```

The app will run at:  
📍 http://127.0.0.1:5000

---

## 🔌 API Endpoints

### 🔹 `GET /health`
Simple health check to verify if the server is running.

**Response:**
```json
{
  "status": "OK"
}
```

---

### 🔹 `POST /predict`

**Request Body:**
```json
{
  "features": [0.1, -1.2, 0.3, 0.0, ..., 500.0]  // 30 values total
}
```

**Response:**
```json
{
  "fraud": true
}
```

---

## 🧪 Running Tests

```bash
pytest tests/test_api.py
```

---

## 👩‍💻 Author

**Tamanna Kapil**  
Aspiring Software Engineer & ML Enthusiast 💡  
[LinkedIn](https://www.linkedin.com/in/yourprofile) • [GitHub](https://github.com/Tamannakapil0904)

---

## 📌 Note

This project uses a publicly available dataset originally published on [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud) and hosted via TensorFlow.

---

## ⭐️ Give it a Star!

If you like this project or found it useful, please ⭐️ the repository to support and motivate further contributions!