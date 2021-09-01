from fastapi import APIRouter, HTTPException
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
        raise HTTPException(status_code=400, detail="The ends of your emoji names should not be surrounded by colons.")

    if provider not in EMOJI_PROVIDERS:
        raise HTTPException(status_code=400, detail="Please specify a valid emoji provider.")

    emoji = Emojipedia.search(emoji_name)

    if emoji is None:
        raise HTTPException(status_code=404, detail=f"I couldn't find a valid emoji for '{emoji_name}.'")

    url: str = None
    for platform in emoji.platforms:
        if provider.lower() == platform.name.lower():
            url = platform.image_url

    if url is None:
        raise HTTPException(status_code=404, detail=f"I couldn't find an image URL for '{emoji_name}' on '{provider}.'")

    return { url }
