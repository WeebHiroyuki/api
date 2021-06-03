from fastapi import APIRouter

router = APIRouter(prefix="/tts", tags=["tts"],)

@router.get("/")
def describe():
    return {
        "message": "TTS Endpoints"
    }