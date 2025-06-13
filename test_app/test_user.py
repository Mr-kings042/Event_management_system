from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_create_user():
    data = {
        "name": "John king",
        "email": "king.doe@example.com"
    }
    response = client.post("/user",data=data)
    assert response.status_code == 201
    data = response.json()
    assert data["detail"] == "User created successfully"


def test_create_user_conflict():
    data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    response = client.post("/user",data=data)
    assert response.status_code == 409
    data = response.json()
    assert data["detail"] == "Username already exists"

def test_create_user_email_conflict():
    data = {
        "name": "Jane ada",
        "email": "john.doe@example.com"
    }
    response = client.post("/user",data=data)
    assert response.status_code == 409
    data = response.json()
    assert data["detail"] == "Email already exists"

def test_get_users():
    response = client.get("/user")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_user_by_id():
    response = client.get("/user/1")
    assert response.status_code == 200
    data = response.json()
    assert data["user retrived successfully"]["id"] == 1
    assert data["user retrived successfully"]["name"] == "John Doe"
    assert data["user retrived successfully"]["email"] == "john.doe@example.com"
def test_get_user_by_id_not_found():
    response = client.get("/user/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User not found"

def test_update_user():
    data = {
        "name": "John Doe Updated",
        "email": "john.doe.updated@example.com"
    }
    response = client.put("/user/1", data=data)
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "User updated successfully"
    updated_user = data["user"]
    assert updated_user["id"] == 1
    assert updated_user["name"] == "John Doe Updated"

def test_update_user_not_found():
    data = {
        "name": "Nonexistent User",
        "email": "nonexistent@example.com"
    }
    response = client.put("/user/999", data=data)
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User with id 999 not found"

def test_delete_user():
    response = client.delete("/user/1")
    assert response.status_code == 204
    

def test_delete_user_not_found():
    response = client.delete("/user/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User not found"