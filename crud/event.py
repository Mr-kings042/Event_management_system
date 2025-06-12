from fastapi import HTTPException, status
from models import Event
from database import events
from schemas.event import EventCreate, EventUpdate



class EventCRUD:
    @staticmethod
    def create_event(event: EventCreate):
        #check if event exists
        for existing_event in events.values():
            if existing_event.title == event.title:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Event with this title already exists"
                )
      
        event_id = len(events) + 1
        event = Event(id=event_id, **event.model_dump())
        events[event_id] = event
        return {"message": "Event created successfully", "event": event}
    @staticmethod
    def get_event(id: int):
        if id not in events:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Event not found"
            )
        return events[id]
    @staticmethod
    def get_events():
        return {"events": list(events.values())}
    @staticmethod
    def update_event(id: int, event: EventUpdate):
        update_event = events.get(id)
        if not update_event:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Event with id {id} not found"
            )
        for field, value in event.model_dump(exclude_unset=True).items():
            setattr(update_event, field, value)
        
        return {"detail": "Event updated successfully", "Event": update_event}
        
    @staticmethod
    def delete_event(id: int):
        if id not in events:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Event not found"
            )
        del events[id]
        return {"message": "Event deleted successfully"}
event_crud = EventCRUD()
    