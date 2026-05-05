import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","deafen_ackerman")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME","snowy2_musicbot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME")
# ---------------------------------------------------------


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002344707828))

# Get this value from @PURVI_HELP_BOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 5536473064))


# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/s%C9%B4%E1%B4%8F%E1%B4%A1%CA%8F-%EA%AD%99-%E1%B4%8D%E1%B4%9Cs%C9%AA%E1%B4%84-----%C9%B4%E1%B4%8F-%E1%B4%80%E1%B4%85%CA%82----%E1%B4%98%CA%80%C9%AA%E1%B4%A0%E1%B4%80%E1%B4%84%CA%8F-%C9%B4%E1%B4%8F%E1%B4%9B%E1%B4%87%EA%9C%B1-05-05-2")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/theteaminfinitybots/NOBITA_MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/theinfinitynetwork")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/theinfinity_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/aa86a4a170e4056923aab-8539d829d6b4771dcf.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/aed4a7a626dd5e1b5dcdd-133ace83ff2672bd63.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/8845649629c4d7025c37f-06bc4b7900f7f640e1.jpg"
STATS_IMG_URL = "https://graph.org/file/0b1f83450b59a65004800-5fd68e26d8fcc38fed.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/0b1f83450b59a65004800-5fd68e26d8fcc38fed.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/f3a0728da34ad80bb1ed6-5c2912a3e77baa8cd2.jpg"
STREAM_IMG_URL = "https://graph.org/file/f3a0728da34ad80bb1ed6-5c2912a3e77baa8cd2.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/f3a0728da34ad80bb1ed6-5c2912a3e77baa8cd2.jpg"
YOUTUBE_IMG_URL = [
    "https://graph.org/file/0cfd31b6d8cf3755cd3c9-7eacaa8ea59650de2a.jpg",
    "https://graph.org/file/9304d01a3ed3632e974d5-96ed16ff307bf8fc7e.jpg",
    "https://graph.org/file/0f7fe7c34140e994aa376-d1efb74f820daa31d5.jpg",
    "https://graph.org/file/25bb7015045251c18f8cb-34b7f869e90b9ed784.jpg",
    "https://graph.org/file/f02053d66b10119c57a95-12c26834e838446116.jpg",
    "https://graph.org/file/a79929395cfa902724f8f-928d61f2407cb99b27.jpg",
]
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/5faa4a08d8a14458c2133-013e9eb15f066be03a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/8845649629c4d7025c37f-06bc4b7900f7f640e1.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/8845649629c4d7025c37f-06bc4b7900f7f640e1.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
