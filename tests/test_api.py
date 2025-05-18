import requests

def test_health():
    response = requests.get("http://127.0.0.1:5000/health")
    assert response.status_code == 200

def test_predict():
    features = [0.0] * 30  # Replace with actual scaled features for real testing
    response = requests.post("http://127.0.0.1:5000/predict", json={"features": features})
    assert response.status_code == 200
    assert "fraud" in response.json()