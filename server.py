import aiohttp
from fastapi import FastAPI
import yaml

from routers.emoji import emoji
from routers.music import music
from routers.tts import tts

app = FastAPI()

with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

if config["modules"]["emoji"]["enabled"]:
    app.include_router(emoji.router)
if config["modules"]["tts"]["enabled"]:
    app.include_router(tts.router)
if config["modules"]["music"]["enabled"]:
    app.include_router(music.router)


@app.get("/")
def root():
    return {
        "detail": "This API is still in development and is nowhere near ready, please come back later."
    }
