from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_appointment():
    dummy_appointment_id = {
    "title": "Test",
    "description": "Test Description",
    "completed": True,
    "due_date": 10-12-2022
    }
    
    response = client.post("/tasks", json=dummy_appointment_id)
    
    assert response.status_code == 200
    assert response.json()["task_id"] == 1