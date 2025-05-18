# 💳 Credit Card Fraud Detection API

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
If you like this project or found it useful, please ⭐️ the repository to support and motivate further contributions!
