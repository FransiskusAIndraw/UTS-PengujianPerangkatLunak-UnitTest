import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user_endpoint():
        response = client.post("/users", json={"name": "API User", "email": "api@example.com"})
        assert response.status_code == 200
        assert response.json()["name"] == "API User"

def test_get_users_endpoint():
        response = client.get("/users")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

def test_update_user_endpoint():
        create_resp = client.post("/users", json={"name": "Old", "email": "old@example.com"})
        user_id = create_resp.json()["id"]
        update_resp = client.put(f"/users/{user_id}", json={"name": "New", "email": "new@example.com"})
        assert update_resp.status_code == 200
        assert update_resp.json()["name"] == "New"