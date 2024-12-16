import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_note():
    response = client.get("/notes/1")
    assert response.status_code == 200
    assert "title" in response.json()
    assert "content" in response.json()
