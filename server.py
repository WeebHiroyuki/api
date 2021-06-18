import aiohttp
from fastapi import FastAPI

from routers.emoji import emoji
from routers.music import music
from routers.tts import tts

app = FastAPI()


app.include_router(emoji.router)
app.include_router(tts.router)
app.include_router(music.router)


@app.get("/")
def root():
    return {
        "detail": "This API is still in development and is nowhere near ready, please come back later."
    }
