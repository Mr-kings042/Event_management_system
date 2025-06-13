from datetime import date
from fastapi import  HTTPException, status
from models import Registration
from schemas.registration import RegistrationCreate
from database import registrations, users, events



class RegisterCrud:
    @staticmethod
    def register_a_user(registration: RegistrationCreate):
           if registration.user_id not in users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
           user = users[registration.user_id]
           if not user.is_active:
                 raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User is not active")
        
           if any(reg.user_id == registration.user_id and reg.event_id == registration.event_id for reg in registrations.values()):
                 raise HTTPException(status_code=status.HTTP_409_CONFLICT,  detail="User already registered for this event")
           #event must be open for registration
           if any(event.id == registration.event_id and not event.is_open  for event in events.values()):
                 raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Event is not open for registration")
           if registration.event_id not in events:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
           
           new_registration = Registration(id = len(registrations) + 1,registration_date= date.today(),  **registration.model_dump())

           registrations[new_registration.id] = new_registration
           return {"message": "Registration successful for the event", "Registration": new_registration}
    
    @staticmethod
    def get_all_registrations():
        return {"message": "All registrations found", "Registrations": list(registrations.values())}
    
    @staticmethod
    def get_registration_for_a_user(user_id: int):
         user_regs = [reg for reg in registrations.values() if reg.user_id == user_id]
         if not user_regs:
               raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User registration not found")
         return {"message": "User registrations found", "Registration": user_regs}
    
   
    


register_crud = RegisterCrud()