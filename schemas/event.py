from typing import Optional
from pydantic import BaseModel
from datetime import date


class EventBase(BaseModel):
    title: str
    date: str = date.today
    location: str

class EventCreate(EventBase):
    is_open: bool = True

class EventUpdate(EventBase):
    title: Optional[str] = None
    date: Optional[str] = None
    location: Optional[str] = None
    is_open:  Optional[bool] = None

class Event(EventBase):
    id: int
    

    