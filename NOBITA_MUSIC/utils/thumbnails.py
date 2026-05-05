import random
from config import YOUTUBE_IMG_URL


async def get_thumb(videoid: str):
    """
    Returns a random thumbnail from config list.
    """
    if isinstance(YOUTUBE_IMG_URL, list):
        return random.choice(YOUTUBE_IMG_URL)
    return YOUTUBE_IMG_URL
    
