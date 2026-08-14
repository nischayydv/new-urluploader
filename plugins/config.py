import os
from os import environ
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    # Required Telegram Bot Credentials
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8021806435:AAFGhQDVA3OXJMmtM74qSSFSQyeeFNRiw2A")
    API_ID = int(os.environ.get("API_ID", 24720215))
    API_HASH = os.environ.get("API_HASH", "c0d3395590fecba19985f95d6300785e")

    # Bot username (optional)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Url_Uploader_NY_Bot")
    SESSION_NAME = "UploaderXNTBot"
    SESSION_STR = ""

    # Download Path
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS")

    # File Limits
    MAX_FILE_SIZE = 2194304000
    TG_MAX_FILE_SIZE = 2194304000
    FREE_USER_MAX_FILE_SIZE = 2194304000
    TG_MIN_FILE_SIZE = 2194304000

    # Chunk Size
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    # Thumbnail
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    # Watermark
    DEF_WATER_MARK_FILE = os.environ.get("DEF_WATER_MARK_FILE", "@UploaderXNTBot")

    # Proxy and Timeouts
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    PROCESS_MAX_TIMEOUT = 3600

    # Logging
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002732334186"))
    LOGGER = logging

    # Admins & Banned
    OWNER_ID = int(os.environ.get("OWNER_ID", "7910994767"))
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    # Database
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Nischay999:Nischay999@cluster0.5kufo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    # Channels
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002465691872")

    # Message Settings
    MAX_MESSAGE_LENGTH = 4096

    # Shortlink
    SHORT_DOMAIN = environ.get("SHORT_DOMAIN", "")
    SHORT_API = environ.get("SHORT_API", "")
    TRUE_OR_FALSE = os.environ.get("TRUE_OR_FALSE", "").lower() == "true"

    # Tutorial / Help Link
    VERIFICATION = os.environ.get("VERIFICATION", "")
    TUTORIAL_LINK = os.environ.get("TUTORIAL_LINK", "https://t.me/How_To_Open_Linkl")

    # Other Custom Values
    ADL_BOT_RQ = {}
    MAX_RESULTS = int(os.environ.get("MAX_RESULTS", "50"))
