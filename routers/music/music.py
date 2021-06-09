import aiohttp
from fastapi import APIRouter

router = APIRouter(
    prefix="/music",
    tags=["music"],
)


@router.get("/")
async def root():
    session = aiohttp.ClientSession()
    async with session.get("https://google.com") as request:
        return request.status
