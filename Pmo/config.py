from os import getenv
from base64 import b64decode


API_ID = int(getenv("API_ID", "6092505"))
API_HASH = getenv("API_HASH", "98d119a0bebd325358589b62461e41a2")
BOT_TOKEN = getenv("BOT_TOKEN", "5922628796:AAEdoXSAlf2aR8iMMypj7LCWY5c3do1bwFs")

LOGS_ID = int(getenv("LOGS_ID", "-1001772777156"))
OWNER_ID = int(getenv("OWNER_ID", "1802485572"))
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001835487855"))
CHANNEL_DB = int(getenv("CHANNEL_DB", "-1001879209028"))

BRANCH = "main"
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwX1BqUzZ2VHM0ZG02cXdSQ2RRa3BucWtTc1IyZ3U0aTJuNGtpUw==").decode("utf-8"),
)
REPO_URL = getenv(
    "REPO_URL",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL09USEZhbWlseS9CYXNlLVJlcG8=").decode("utf-8"),
)
