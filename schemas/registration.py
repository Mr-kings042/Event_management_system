from datetime import date
from pydantic import BaseModel


class RegistrationBase(BaseModel):
    user_id: int
    event_id: int


class RegistrationCreate(RegistrationBase):
    pass

class Registration(RegistrationBase):
    id: str
    registration_date: date = date.today()
    attended: bool = False