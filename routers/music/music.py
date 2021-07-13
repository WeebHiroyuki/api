import json

import aiohttp
from bs4 import BeautifulSoup
from fastapi import APIRouter, HTTPException

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


def unescape(text):
    return text.encode("utf-8").decode("unicode_escape")


def beautify_playlist(text):
    unescaped = unescape(text)
    remove_start = unescaped.split('2ccontributors":"')
    remove_ending = remove_start[1].split('"}</script>')
    return remove_ending[0]


def reformat_playlist(text):
    jsondata = json.loads(text)
    maindata = jsondata["d"][0]
    tracks = maindata["relationships"]["tracks"]["data"]
    curatorName = "N/A"
    if "curatorName" in maindata["attributes"]:
        curatorName = maindata["attributes"]["curatorName"]
    curatorSocialHandle = "N/A"
    if "curatorSocialHandle" in maindata["attributes"]:
        curatorSocialHandle = maindata["attributes"]["curatorSocialHandle"]
    data = {
        "playlistAuthor": {
            "displayName": curatorName,
            "socialHandle": curatorSocialHandle,
        },
        "playlistName": maindata["attributes"]["name"],
        "playlistURL": maindata["attributes"]["url"],
        "playlistCover": {
            "png": maindata["attributes"]["artwork"]["url"]
            .replace("{w}", str(maindata["attributes"]["artwork"]["width"]))
            .replace("{h}", str(maindata["attributes"]["artwork"]["height"]))
            .replace("{f}", "png"),
            "jpg": maindata["attributes"]["artwork"]["url"]
            .replace("{w}", str(maindata["attributes"]["artwork"]["width"]))
            .replace("{h}", str(maindata["attributes"]["artwork"]["height"]))
            .replace("{f}", "jpg"),
            "webp": maindata["attributes"]["artwork"]["url"]
            .replace("{w}", str(maindata["attributes"]["artwork"]["width"]))
            .replace("{h}", str(maindata["attributes"]["artwork"]["height"]))
            .replace("{f}", "webp"),
            "gif": maindata["attributes"]["artwork"]["url"]
            .replace("{w}", str(maindata["attributes"]["artwork"]["width"]))
            .replace("{h}", str(maindata["attributes"]["artwork"]["height"]))
            .replace("{f}", "gif"),
        },
        "playlistID": maindata["id"],
        "trackCount": maindata["attributes"]["trackCount"],
        "lastModifiedDate": maindata["attributes"]["lastModifiedDate"],
        "tracks": [],
    }

    for index, track in enumerate(tracks):
        composerName = "N/A"
        if "composerName" in track["attributes"]:
            composerName = track["attributes"]["composerName"]
        newtrack = {
            "trackID": track["id"],
            "trackIndex": index + 1,
            "trackName": track["attributes"]["name"],
            "trackURL": track["attributes"]["url"],
            "trackAlbum": {
                "id": track["attributes"]["url"].split("/")[6].split("?i=")[0],
                "url": track["attributes"]["url"].split("?i=")[0],
                "name": track["attributes"]["albumName"],
            },
            "trackArtist": {
                "id": track["attributes"]["artistUrl"].split("/")[6],
                "url": track["attributes"]["artistUrl"],
                "name": track["attributes"]["artistName"],
            },
            "composerName": composerName,
            "trackArtwork": {
                "png": track["attributes"]["artwork"]["url"]
                .replace("{w}", str(track["attributes"]["artwork"]["width"]))
                .replace("{h}", str(track["attributes"]["artwork"]["height"]))
                .replace("{f}", "png"),
                "jpg": track["attributes"]["artwork"]["url"]
                .replace("{w}", str(track["attributes"]["artwork"]["width"]))
                .replace("{h}", str(track["attributes"]["artwork"]["height"]))
                .replace("{f}", "jpg"),
                "webp": track["attributes"]["artwork"]["url"]
                .replace("{w}", str(track["attributes"]["artwork"]["width"]))
                .replace("{h}", str(track["attributes"]["artwork"]["height"]))
                .replace("{f}", "webp"),
                "gif": track["attributes"]["artwork"]["url"]
                .replace("{w}", str(track["attributes"]["artwork"]["width"]))
                .replace("{h}", str(track["attributes"]["artwork"]["height"]))
                .replace("{f}", "gif"),
                "color": track["attributes"]["artwork"]["bgColor"],
            },
            "trackDurationInMS": track["attributes"]["durationInMillis"],
            "trackReleaseDate": track["attributes"]["releaseDate"],
            "trackISRC": track["attributes"]["isrc"],
            "trackGenres": track["attributes"]["genreNames"],
        }
        data["tracks"].append(newtrack)

    return data


def beautify_album(text):
    unescaped = unescape(text)
    remove_start = unescaped.split('2caudio-extras":"')
    remove_ending = remove_start[1].split('"}</script>')
    return remove_ending[0]


def reformat_album(text):
    jsondata = json.loads(text)
    maindata = jsondata["d"][0]
    tracks = maindata["relationships"]["tracks"]["data"]
    data = {
        "albumID": maindata["id"],
        "albumName": maindata["attributes"]["name"],
        "albumURL": maindata["attributes"]["url"],
        "albumArtist": {
            "id": maindata["relationships"]["artists"]["data"][0]["id"],
            "url": maindata["relationships"]["artists"]["data"][0]["attributes"]["url"],
            "name": maindata["relationships"]["artists"]["data"][0]["attributes"][
                "name"
            ],
        },
        "albumArtwork": {
            "png": maindata["attributes"]["artwork"]["url"]
            .replace("{w}", str(maindata["attributes"]["artwork"]["width"]))
            .replace("{h}", str(maindata["attributes"]["artwork"]["height"]))
            .replace("{f}", "png"),
            "jpg": maindata["attributes"]["artwork"]["url"]
            .replace("{w}", str(maindata["attributes"]["artwork"]["width"]))
            .replace("{h}", str(maindata["attributes"]["artwork"]["height"]))
            .replace("{f}", "jpg"),
            "webp": maindata["attributes"]["artwork"]["url"]
            .replace("{w}", str(maindata["attributes"]["artwork"]["width"]))
            .replace("{h}", str(maindata["attributes"]["artwork"]["height"]))
            .replace("{f}", "webp"),
            "gif": maindata["attributes"]["artwork"]["url"]
            .replace("{w}", str(maindata["attributes"]["artwork"]["width"]))
            .replace("{h}", str(maindata["attributes"]["artwork"]["height"]))
            .replace("{f}", "gif"),
            "color": maindata["attributes"]["artwork"]["bgColor"],
        },
        "trackCount": maindata["attributes"]["trackCount"],
        "albumReleaseDate": maindata["attributes"]["releaseDate"],
        "recordLabel": maindata["attributes"]["recordLabel"],
        "upc": maindata["attributes"]["upc"],
        "isSingle": maindata["attributes"]["isSingle"],
        "genreNames": maindata["attributes"]["genreNames"],
        "tracks": [],
    }

    for index, track in enumerate(tracks):
        composerName = "N/A"
        if "composerName" in track["attributes"]:
            composerName = track["attributes"]["composerName"]
        newtrack = {
            "trackID": track["id"],
            "trackIndex": index + 1,
            "trackName": track["attributes"]["name"],
            "trackURL": track["attributes"]["url"],
            "composerName": composerName,
            "trackDurationInMS": track["attributes"]["durationInMillis"],
            "trackReleaseDate": track["attributes"]["releaseDate"],
            "trackISRC": track["attributes"]["isrc"],
            "trackGenres": track["attributes"]["genreNames"],
        }
        data["tracks"].append(newtrack)

    return data


def fetch_track_from_album(text, track_id):
    newtrack = None
    for track in text["tracks"]:
        if track["trackID"] == track_id:
            newtrack = track
    if newtrack is None:
        return None

    text.pop("tracks", None)
    text.pop("trackCount", None)
    text.pop("isSingle", None)
    text.pop("genreNames", None)
    text["track"] = newtrack
    text["track"].pop("trackIndex", None)
    return text


@router.get("/applemusic/playlist/")
async def apple_music_playlist(playlist_id: str, country: str = "us"):
    """
    Get JSON data about an Apple Music playlist.

    This endpoint is still in beta, and errors may occur.

    ----------

    playlist_id: The id of the playlist to retrieve.

    country: Optional country to use when retrieving the playlist. Defaults to US.

    ----------
    Returns: A JSON object containing information about the playlist.
    """
    url = (
        "https://music.apple.com/" + country + "/playlist/" + "kao" + "/" + playlist_id
    )
    results = await get_initial_apple_music_data(url)
    if results is None:
        raise HTTPException(status_code=404, detail="Playlist not found.")
    beautified = beautify_playlist(results)
    reformatted = reformat_playlist(beautified)
    return reformatted


@router.get("/applemusic/album/")
async def apple_music_album(album_id: str, country: str = "us"):
    """
    Get JSON data about an Apple Music album.

    This endpoint is still in beta, and errors may occur.

    ----------

    album_id: The id of the album to retrieve.

    country: Optional country to use when retrieving the album. Defaults to US.

    ----------
    Returns: A JSON object containing information about the album.
    """
    url = "https://music.apple.com/" + country + "/album/" + "kao" + "/" + album_id
    results = await get_initial_apple_music_data(url)
    if results is None:
        raise HTTPException(status_code=404, detail="Album not found.")
    beautified = beautify_album(results)
    reformatted = reformat_album(beautified)
    return reformatted


@router.get("/applemusic/track/")
async def apple_music_track(album_id: str, track_id: str, country: str = "us"):
    """
    Get JSON data about an Apple Music track.

    This endpoint is still in beta, and errors may occur.

    ----------

    album_id: The id of the album to retrieve.

    track_id: The id of the track to retrieve.

    country: Optional country to use when retrieving the track. Defaults to US.

    ----------
    Returns: A JSON object containing information about the track.
    """
    url = (
        "https://music.apple.com/"
        + country
        + "/album/"
        + "kao"
        + "/"
        + album_id
        + "?i="
        + track_id
    )
    results = await get_initial_apple_music_data(url)
    if results is None:
        raise HTTPException(status_code=404, detail="Track not found.")
    beautified = beautify_album(results)
    reformatted = reformat_album(beautified)
    track = fetch_track_from_album(reformatted, track_id)
    if track is None:
        raise HTTPException(status_code=404, detail="Track not found.")
    return track
