from database import speakers
from schemas.speaker import Speaker

class SpeakerService:
    @staticmethod
    def preload_speakers():
       if not speakers:
         speakers[1] = Speaker(id=1, name="Dr. Jane Njoku", topic="AI in Healthcare")
         speakers[2] = Speaker(id=2, name="Prof. John Kings", topic="Cybersecurity Trends")
         speakers[3] = Speaker(id=3, name="Ms. Ada Omeh", topic="The Future of Programming")
         speakers[4] = Speaker(id=4, name="Dr. Kingsley ", topic="Machine Learning")
       return speakers


speaker_service = SpeakerService()
speaker_service.preload_speakers()
    