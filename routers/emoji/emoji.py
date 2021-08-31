from fastapi import APIRouter
from emojipedia import Emojipedia
from constants import EMOJI_PROVIDERS

router = APIRouter(
    prefix="/emoji",
    tags=["emoji"],
)


@router.get("/")
def root():
    return {
        "detail": "This is the base URL for the emoji endpoints. Check the documentation for more information."
    }

@router.get("/:{emoji_name}")
def resolve_emoji_url(emoji_name: str, provider: str):
    if emoji_name.startswith(":") or emoji_name.endswith(":"):
        return {
            "detail": "Please omit any colons from the ends of your emoji name."
        }

    if provider not in EMOJI_PROVIDERS:
        return {
            "detail": "Please specify a valid platform."
        }

    emoji = Emojipedia.search(emoji_name)

    if emoji is None:
        return {
            "detail": f"The requested emoji ('{emoji_name}') could not be found."
        }

    url: str = None
    for platform in emoji.platforms:
        if provider.lower() == platform.name.lower():
            url = platform.image_url

    if url is None:
        return {
            "detail": f"I couldn't find a platform where the {emoji_name} emoji is available."
        }

    return { url }
