from fastapi import APIRouter

router = APIRouter(
    prefix="/emoji",
    tags=["emoji"],
)


@router.get("/")
def root():
    return {"message": "Emoji Endpoints"}
