from os import getenv
from base64 import b64decode


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")

OWNER_ID = int(getenv("OWNER_ID", ""))
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
CHANNEL_DB = int(getenv("CHANNEL_DB", ""))

GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwX1BqUzZ2VHM0ZG02cXdSQ2RRa3BucWtTc1IyZ3U0aTJuNGtpUw==").decode("utf-8"),
)
REPO_URL = getenv(
    "REPO_URL",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL09USEZhbWlseS9CYXNlLVJlcG8=").decode("utf-8"),
)
