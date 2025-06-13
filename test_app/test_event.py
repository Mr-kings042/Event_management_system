from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_event():
    data = {
        "title": "Tech Conference",
        "date": "2023-10-01",
        "location": "New York",
        "is_open": True
    }
    response = client.post("/event", data=data)
    assert response.status_code == 201
    data = response.json()
    assert data["message"] == "Event created successfully"

def test_get_events():
    response = client.get("/event")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["events"], list)

def test_get_events_not_found():
    response = client.get("/event/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Event not found"

def test_get_event_by_id():
    response = client.get("/event/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Tech Conference"
    assert data["location"] == "New York"

def test_update_event():
    data = {
        "title": "Tech Conference Updated",
        "date": "2023-10-02",
        "location": "San Francisco",
        "is_open": False
    }
    response = client.put("/event/1", data=data)
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Event updated successfully"

def test_update_event_not_found():
    data = {
        "title": "Nonexistent Event",
        "date": "2023-10-03",
        "location": "Unknown",
        "is_open": True
    }
    response = client.put("/event/999", data=data)
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Event with id 999 not found"

def test_delete_event():
    response = client.delete("/event/1")
    assert response.status_code == 204

def test_delete_event_not_found():
    response = client.delete("/event/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Event not found"

def test_close_event_registration_event_not_found():
    response = client.patch("/event/1/close")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Event not found"

def test_close_event_registration():
    data = {
        "title": "Tech Conference",
        "date": "2023-10-01",
        "location": "New York",
        "is_open": True
    }
    response = client.post("/event", data=data)
    assert response.status_code == 201

    response = client.patch("/event/1/close")
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Event with ID 1 closed successfully"
    
    # Verify that the event is now closed
    response = client.get("/event/1")
    assert response.status_code == 200
    event_data = response.json()
    assert event_data["is_open"] is False