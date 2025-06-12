# Event Management API System
An Event Management API system built with FastAPI. It allows users to register for events, manage event attendance, and retrieve user and event-related data.

## Features
- Create users and events
- Retrieve users and events
- Deactivate User
- Close Event registration
- Register users for events (if open)
- Prevent duplicate registrations
- Mark user attendance
- Get a list of attendees
- Get user who attended an event
- Get registrations for a user

# Getting Started
## How to Run This Project (Step-by-Step)

### Prerequisites

Before you begin, make sure you have:

- Python 3.8 or higher installed
- `pip` (Python package manager)

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/event-management-api.git
cd event_management_system
```

### step 2: Create a Virtual Environment
```bash
python -m venv venv
(for mac/linux)
source venv/bin/activate
(for windows)
venv\Scripts\activate
```

### Step 3: Install Dependencies from requirement.txt

```bash
pip install -r requirements.txt
```
### Step 4: Run the App
```bash
uvicorn main:app --reload
```

--- You should see output indicating the app is running at:


INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

### Step 5: Access the API Docs
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc


# API Endpoints

## Users Endpoints
| Method | Endpoint           | Description         |
| ------ | ------------------ | ------------------- |
| POST   | `/users/`          | Create a new user   |
| GET    | `/users/`          | Get all users       |
| GET    | `/users/{user_id}` | Get a specific user |
| PUT | `/users/{user_id}` | update a specific user details |
| DELETE | `/users/{user_id}` | delete a user
| PATCH | `/users/{user_id}` | Deactivate a user |

## Events Endpoints
| Method | Endpoint             | Description          |
| ------ | -------------------- | -------------------- |
| POST   | `/events/`           | Create a new event   |
| GET    | `/events/`           | Get all events       |
| GET    | `/events/{event_id}` | Get a specific event |
| PUT | `/events/{event_id}` | update a specific event details |
| DELETE | `/events/{event_id}` | delete an event
| PATCH | `/events/{event_id}` | Close Event registration |

## Registrations Endpoints
| Method | Endpoint                         | Description                            |
| ------ | -------------------------------- | -------------------------------------- |
| POST   | `/register/`                 | Register a user for an event           |
| GET    | `/register/`                 | Get all registrations                  |
| GET    | `/register/{user_id}`        | Get registrations for a specific user  |
| PUT  | `/register/{event_id}/attendance` | Mark attendance for a user             |
| GET    | `/register/attendees/all`        | Get all attendees (users who attended) |
| GET    | `/register/attendees/{event_id}`        | Get all attendees (users who attended an event) |
| GET    | `/register/attendees/event/users`        | Get users who attended at least on event |


# Testing
You can Test the endpoints using:
- Swagger Docs at /docs
- ReDoc at /redoc
- Postman or Thunder Client

# Project structure

├── main.py
├── models.py
├── schemas/
│   ├── user.py
│   ├── event.py
│   └── registration.py
│   └── speaker.py
├── crud/
│   └── event.py
│   └── registration.py
│   └── user.py
├── routes/
│   └── event.py
│   └── registration.py
│   └── user.py
│   └── speaker.py
├── services/
│   └── registration.py
│   └── event.py
├── database.py
└── README.md
└── Requirement.txt

