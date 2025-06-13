from fastapi import APIRouter, status, Form
from schemas.event import EventCreate, EventUpdate
from models import Event
from crud.event import event_crud
from services.event import event_service

event_router = APIRouter()

@event_router.post("", status_code=status.HTTP_201_CREATED)
def create_event(event_data: EventCreate = Form(...)):
    return event_crud.create_event(event_data)

@event_router.get("", status_code=status.HTTP_200_OK)
def get_events():
    return  event_crud.get_events()

@event_router.get("/{id}", status_code=status.HTTP_200_OK)
def get_event_by_id(id: int):
    return event_crud.get_event(id)


@event_router.put("/{id}", status_code=status.HTTP_200_OK)
def update_event(id: int, event_data: EventUpdate = Form(...)):
    return event_crud.update_event(id, event_data)  

@event_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(id: int):
    return event_crud.delete_event(id)

@event_router.patch("/{id}/close", status_code=status.HTTP_200_OK)
def close_event_registration(id: int):
    return event_service.close_event_registration(id)