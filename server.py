import sentry_sdk
import yaml
from fastapi import FastAPI

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

if config["general"]["sentry"]:
    sentry_sdk.init(config["general"]["sentry"], traces_sample_rate=1.0)


@app.get("/")
def root():
    return {
        "detail": "This is the base url for this API. Check out the documentation for more information."
    }