import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_health_check():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json()["status"] == "OK"

def test_predict_endpoint():
    # Send sample data with 30 features
    payload = {
        "features": [
            0.1, -0.3, 0.5, -0.2, 0.0,
            0.6, 0.2, 0.4, 0.3, 500.0,
            0.3, -0.4, 0.1, 0.2, 0.5,
            -0.1, 0.0, 0.6, 0.7, 1.0,
            0.2, 0.1, 0.9, -0.6, -0.7,
            -0.5, 0.4, 0.8, 1.2, -1.0
        ]
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/predict", data=json.dumps(payload), headers=headers)

    assert response.status_code == 200
    assert "fraud" in response.json()
    assert isinstance(response.json()["fraud"], bool)