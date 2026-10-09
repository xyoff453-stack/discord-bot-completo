import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN", "")
PREFIX = os.getenv("DISCORD_PREFIX", "!")
OWNER_IDS = tuple(
    int(value.strip())
    for value in os.getenv("OWNER_IDS", "").split(",")
    if value.strip()
)
GUILD_ID = int(os.getenv("GUILD_ID", "0")) or None
