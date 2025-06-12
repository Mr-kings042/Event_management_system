from fastapi import FastAPI
from routes.user import user_router
from routes.event import event_router
from routes.registration import register_router
from routes.speaker import speaker_router
from services.speaker import speaker_service






app = FastAPI(title="Event Management API System")


@app.get("/")
async def root():
    return {"message": "Welcome to Event Management System API", "version": "1.0", "speakers":speaker_service.preload_speakers()
 }
speaker_service.preload_speakers()

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(event_router, prefix="/event", tags=["event"])
app.include_router(register_router, prefix="/register", tags=["register"])
app.include_router(speaker_router, prefix="/speaker", tags=["speaker"])

