from config import YOUTUBE_IMG_URL


async def get_thumb(videoid: str):
    """
    Returns static thumbnail from config.
    No processing, no caching, no API calls.
    """
    return YOUTUBE_IMG_URL
