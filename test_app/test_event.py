from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# def test_close_event_registration():
#     # Create an event first
#     event_data = {
#         "name": "Test Event",
#         "description": "This is a test event",
#         "date": "2023-10-01",
#         "location": "Test Location"
#     }
#     response = client.post("/event", data=event_data)
#     assert response.status_code == 201
#     event_id = response.json()["id"]

#     # Close the event registration
#     response = client.patch(f"/event/{event_id}/close")
#     assert response.status_code == 200
#     data = response.json()
#     assert data["detail"] == f"Event with ID {event_id} closed successfully"

#     # Verify that the event is closed
#     response = client.get(f"/event/{event_id}")
#     assert response.status_code == 200
#     event = response.json()
#     assert not event["is_open"]
