from fastapi import FastAPI

from routers.emoji import emoji
from routers.tts import tts

app = FastAPI()


app.include_router(emoji.router)
app.include_router(tts.router)


@app.get("/")
async def root():
    return {"message": "This API is still in development and is nowhere near ready, please come back later."}
