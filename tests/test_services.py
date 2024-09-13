import requests

def test_account_service():
    response = requests.get("http://localhost:5000/accounts")
    assert response.status_code == 200

def test_api_gateway():
    response = requests.get("http://localhost:5001/status")
    assert response.status_code == 200

def test_notification_service():
    response = requests.get("http://localhost:5002/notifications")
    assert response.status_code == 200

def test_trading_service():
    response = requests.get("http://localhost:5003/trades")
    assert response.status_code == 200

def test_wallet_service():
    response = requests.get("http://localhost:5004/wallets")
    assert response.status_code == 200
