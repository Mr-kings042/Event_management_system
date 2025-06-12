from fastapi import HTTPException,status
from database import registrations, users
from schemas.user import User

class RegisterService:

 
    @staticmethod
    def mark_attendance(user_id: int,event_id: int):
        
            if event_id not in registrations:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event Registration not found")    
            #check if user is active
            if not users[user_id].is_active:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User is not active")
            #check if event is still avaliable or deleted
            if not registrations:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No registrations found")
        #   check if user is registered for the event
            if user_id not in registrations:
                 raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Registration not found")
            if registrations[user_id].event_id != event_id:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User is not registered for this event")    
          #mark attendance for the user
            registrations[user_id].attended = True

            return {"message": "Attendance marked for the user", "Registration": registrations[user_id]}  

#mark attendance for user registered for an event and mark only once for the event

    @staticmethod
    def get_all_attendees():
        attendees = [
             User(
            id=users[reg.user_id].id,
            name=users[reg.user_id].name,
            email=users[reg.user_id].email,
            is_active=users[reg.user_id].is_active
        ).dict()
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