""" A test file for our main.py equivalent in src """

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_read_main():
    """ Testing our root endpoint """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
