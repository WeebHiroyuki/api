from fastapi import APIRouter

router = APIRouter(prefix="/music", tags=["music"],)

@router.get("/")
def describe():
    return {
        "message": "Music Endpoints"
    }