from fastapi import status, HTTPException
from database import events
class EventService:
    @staticmethod
    def close_event_registration(id: int):
       if id not in events:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Event not found"
            )
       events[id].is_open = False
       return {"detail": f"Event with ID {id} closed successfully"}
    

event_service = EventService()