from fastapi import HTTPException,status
from database import registrations, users
from schemas.user import User

class RegisterService:

 
    @staticmethod
    def mark_attendance(user_id: int,event_id: int):
            if event_id not in registrations:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event Registration not found")      
            registration = None  
            for reg in registrations.values():
                if reg.user_id == user_id and reg.event_id == event_id:
                    registration = reg
                    break
            if not registration:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Registration not found for this event")
            if registration.attended == True:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Attendance already marked for this user for this event")
            registration.attended = True

            return {"message": "Attendance marked for the user", "Registration": registrations[user_id]}  


    @staticmethod
    def get_all_attendees():
        attendees = [
             User(
            id=users[reg.user_id].id,
            name=users[reg.user_id].name,
            email=users[reg.user_id].email,
            is_active=users[reg.user_id].is_active
        ).model_dump()
            for reg in registrations.values() if reg.attended and(user := users.get(reg.user_id))]
        if not attendees:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No attendees found")
        
        return {"message": "Attendees found", "Attendees":attendees}
    
    @staticmethod
    def get_all_attendance_for_event(event_id: int):
        event_registrations = [reg for reg in registrations.values() if reg.event_id == event_id and reg.attended]
        if not event_registrations:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No attendance found for the event")
        
        attendees = [
            User(
                id=users[reg.user_id].id,
                name=users[reg.user_id].name,
                email=users[reg.user_id].email,
                is_active=users[reg.user_id].is_active
            ).dict() for reg in event_registrations if (user := users.get(reg.user_id))
        ]
        
        return {"message": "Event attendance found", "Attendees": attendees}
    #Filter users who attended at least one event
    @staticmethod
    def get_users_who_attended_at_least_one_event():
        attendees = [
            User(
                id=users[reg.user_id].id,
                name=users[reg.user_id].name,
                email=users[reg.user_id].email,
                is_active=users[reg.user_id].is_active
            ).dict() for reg in registrations.values() if reg.attended and (user := users.get(reg.user_id))
        ]
        
        if not attendees:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found who attended at least one event")
        
        return {"message": "Users who attended at least one event found", "Attendees": attendees}
register_service = RegisterService()