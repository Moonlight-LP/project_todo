import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_appointments():
    response = client.get("/appointments")
    assert response.status_code == 200
    assert response.json() == {}
    
def test_create_appointment():
    appointment_id_data = {
    "title": "Test",
    "description": "Test Description",
    "completed": True,
    "due_date": 2022-10-12
    }
    
    response = client.post("/appointments", json=appointment_id_data)
    
    assert response.status_code == 200
    assert response.json()["appointment_id"] == str(1)
    
def test_update_appointment_():
    updated_appointment_data = {
        "title": "Updated",
        "description": "This is an updated test appointment",
        "completed": False,
        "due_date": "2023-04-22"
    }
    response = client.put("/appointments/1", json=updated_appointment_data)
    assert response.status_code == 200

def test_delete_appointment():
    response = client.delete("/appointments/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Appointment deleted"