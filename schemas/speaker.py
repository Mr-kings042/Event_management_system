from pydantic import BaseModel

class Speaker(BaseModel):
    id: int
    name: str
    topic: str
    