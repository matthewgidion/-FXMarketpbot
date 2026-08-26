import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
# Use env vars for API keys too
FCS_API_KEY = os.getenv("FCS_API_KEY")
