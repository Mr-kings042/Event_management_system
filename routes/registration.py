from fastapi import APIRouter,status,Form
from crud.registration import register_crud
from schemas.registration import RegistrationCreate
from services.registration import register_service


register_router = APIRouter()

@register_router.post("", status_code=status.HTTP_201_CREATED)
def register_for_event(registration_data: RegistrationCreate = Form(...)):
    return register_crud.register_a_user(registration_data)

@register_router.get("", status_code=status.HTTP_200_OK)
def get_all_registrations():
    return register_crud.get_all_registrations()

@register_router.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_registration_by_a_user(user_id: int):
    return register_crud.get_registration_for_a_user(user_id)

@register_router.put("/{event_id}/attendance", status_code=status.HTTP_200_OK)
def mark_attendance(user_id: int, event_id: int):
    return register_service.mark_attendance(user_id, event_id)

@register_router.get("/attendee/{event_id}", status_code=status.HTTP_200_OK)
def get_attendees_for_an_event(event_id: int):
    return register_service.get_all_attendance_for_event(event_id)

@register_router.get("/attendees/all", status_code=status.HTTP_200_OK)
def get_all_attendees():
    return register_service.get_all_attendees()

@register_router.get("/attendee/event/users", status_code=status.HTTP_200_OK)
def get_users_who_attended_at_least_one_event():
    return register_service.get_users_who_attended_at_least_one_event()