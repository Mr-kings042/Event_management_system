from fastapi.testclient import TestClient
from main import app
from database import users, events


client = TestClient(app)

def test_register_for_event():
    users.clear()
    events.clear()
    #create a user and an event first
    user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    client.post("/user", data=user_data)
    event_data = {
        "title": "Tech Summit",
        "date": "2023-10-15",
        "location": "San Francisco",
        "is_open": True
    }
    client.post("/event", data=event_data)


    registration_data = {
        "user_id": 1,
        "event_id": 1,
        "registration_date": "2023-10-01",
        "attended": False
    }
    response = client.post("/register", data=registration_data)
    assert response.status_code == 201
    data = response.json()
    assert data["message"] == "Registration successful for the event"


def test_register_for_event_user_not_found():
    data = {
        "user_id": 2,
        "event_id": 1,
        "attended": True
    }
    response = client.post("/register", data=data)
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User not found"

def test_get_all_registrations():
    response = client.get("/register")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["Registrations"], list)

def test_get_registration_by_a_user():
    response = client.get("/register/1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["Registration"], list)
    assert len(data["Registration"]) > 0

def test_get_registration_by_a_user_not_found():
    response = client.get("/register/user/999")
    assert response.status_code == 404
  

def test_register_for_event_already_registered():
    data = {
        "user_id": 1,
        "event_id": 1,
        "attended": True
    }
    response = client.post("/register", data=data)
    assert response.status_code == 409
    data = response.json()
    assert data["detail"] == "User already registered for this event"

def test_mark_attendance():

    response = client.put("/register/1/attendance?user_id=1")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Attendance marked for the user"
    assert data["Registration"]["attended"] is True

def test_mark_attendance_event_not_registered():
    response = client.put("/register/2/attendance?user_id=2")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Event Registration not found"

def test_mark_attendance_user_not_registered():
    response = client.put("/register/1/attendance?user_id=999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User Registration not found for this event"

def test_get_all_attendees():
    response = client.get("/register/attendees/all")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["Attendees"], list)
    assert len(data["Attendees"]) > 0
