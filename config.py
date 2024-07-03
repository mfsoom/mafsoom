from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", 25442050))
API_HASH = getenv("API_HASH", "e81d29a55a67bb6357c9b8af7b769f9b")

BOT_TOKEN = getenv("BOT_TOKEN", "6437907769:AAEgVIwRLzPPcoWZvTn8cFgkR1stTrMVJBM")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mohammadtaleb2012t:hamoda7@cluster0.xwc4uff.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 7190917175))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/UUUJD")
