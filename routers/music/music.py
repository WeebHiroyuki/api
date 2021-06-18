import aiohttp
import json
from fastapi import APIRouter, HTTPException
from bs4 import BeautifulSoup

router = APIRouter(
    prefix="/music",
    tags=["music"],
)


@router.get("/")
async def root():
    return {
        "detail": "This is the base URL for the music endpoints. Check the documentation for more information."
    }


async def get_initial_apple_music_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                webpage = BeautifulSoup(await response.text(), "html.parser")
                results = webpage.find(id="shoebox-media-api-cache-amp-music")
                if results:
                    return str(results)
            return


def unescape(text):
    return text.encode("utf-8").decode("unicode_escape")


def beautify_playlist(text):
    unescaped = unescape(text)
    remove_start = unescaped.split('2ccontributors":"')
    remove_ending = remove_start[1].split('"}</script>')
    return remove_ending[0]


def beautify_album(text):
    unescaped = unescape(text)
    remove_start = unescaped.split('2caudio-extras":"')
    remove_ending = remove_start[1].split('"}</script>')
    return remove_ending[0]


@router.get("/applemusic/playlist/")
async def apple_music_playlist(user: str, playlist_id: str, country: str = "us"):
    """
    Get JSON data about an apple music playlist.
    """
    url = "https://music.apple.com/" + country + "/playlist/" + user + "/" + playlist_id
    results = await get_initial_apple_music_data(url)
    if results is None:
        raise HTTPException(status_code=404, detail="Playlist not found.")
    beautified = beautify_playlist(results)
    json_data = json.loads(beautified)
    return json_data


@router.get("/applemusic/album/")
async def apple_music_album(name: str, album_id: str, country: str = "us"):
    """
    Get JSON data about an apple music album.
    """
    url = "https://music.apple.com/" + country + "/album/" + name + "/" + album_id
    results = await get_initial_apple_music_data(url)
    if results is None:
        raise HTTPException(status_code=404, detail="Album not found.")
    beautified = beautify_album(results)
    json_data = json.loads(beautified)
    return json_data


@router.get("/applemusic/album/")
async def apple_music_track(
    name: str, album_id: str, track_id: str, country: str = "us"
):
    """
    Get JSON data about an apple music album.
    """
    url = (
        "https://music.apple.com/"
        + country
        + "/album/"
        + name
        + "/"
        + album_id
        + "?i="
        + track_id
    )
    results = await get_initial_apple_music_data(url)
    if results is None:
        raise HTTPException(status_code=404, detail="Track not found.")
    beautified = beautify_album(results)
    json_data = json.loads(beautified)
    return json_data
