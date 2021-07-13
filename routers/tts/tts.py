from fastapi import APIRouter

router = APIRouter(
    prefix="/tts",
    tags=["tts"],
)


@router.get("/")
def root():
    return {
        "message": "This is the base URL for the TTS endpoints. Check the documentation for more information."
    }
