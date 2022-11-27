import logging
import asyncio
import pyromod.listen
from logging.handlers import RotatingFileHandler

from pyrogram import Client
from Pmo.config import API_ID, API_HASH, BOT_TOKEN


app = Client(
    name="Bottings",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "Pmo.plugins"},
)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logs = logging.getLogger(__name__)
loop = asyncio.get_event_loop_policy().get_event_loop()
