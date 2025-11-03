from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_api():
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json()["result"] == 5

def test_subtract_api():
    response = client.get("/subtract?a=7&b=2")
    assert response.status_code == 200
    assert response.json()["result"] == 5

def test_multiply_api():
    response = client.get("/multiply?a=3&b=4")
    assert response.status_code == 200
    assert response.json()["result"] == 12

def test_divide_api():
    response = client.get("/divide?a=10&b=2")
    assert response.status_code == 200
    assert response.json()["result"] == 5

