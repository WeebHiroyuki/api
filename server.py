from fastapi import FastAPI
from emoji import emoji

router = FastAPI()

@router.get("/")
def describe():
    return {"message": "This API is still in development and is nowhere near ready, please come back later."}