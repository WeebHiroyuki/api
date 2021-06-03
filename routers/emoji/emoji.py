from fastapi import APIRouter

router = APIRouter(prefix="/emoji", tags=["emoji"],)

@router.get("/")
def describe():
    return {
        "message": "Emoji Endpoints"
    }