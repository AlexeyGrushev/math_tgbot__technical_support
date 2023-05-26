import os
from dotenv import load_dotenv


try:
    load_dotenv()
finally:
    TOKEN = os.getenv("BOT_TOKEN")
    SUPPORT_CHAT = os.getenv("SUPPORT_CHAT_ID")
    DB_NAME = os.getenv("DB_NAME")
