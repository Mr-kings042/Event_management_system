from fastapi import APIRouter,status
from schemas.speaker import Speaker
from services.speaker import speaker_service


speaker_router = APIRouter()

@speaker_router.get("/",status_code=status.HTTP_200_OK)
def view_all_speakers():
    return speaker_service.preload_speakers()