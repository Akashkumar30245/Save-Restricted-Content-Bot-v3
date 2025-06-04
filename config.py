# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "23626191")
API_HASH = os.getenv("API_HASH", "a1416a7b389a7d6d4466ae5e014f7518")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8166451122:AAGsNXECncBD1zW5XqbPa33Rg_EZgR24d2o")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://freestudymaterial2024:mc2pGRMs35YVlbLf@cluster0.fdhci3r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "7925792971").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002524058716")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-10012345567")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "20"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "5000"))
JOIN_LINK = os.getenv("JOIN_LINK", "https://t.me/team_spy_pro") # this link for start command message
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "@Thakur_Ji30245")

