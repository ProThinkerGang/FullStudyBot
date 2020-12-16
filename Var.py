import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class var:
  API_ID = os.getenv("API_ID", None) # API_ID
  API_HASH = os.getenv("API_HASH", None) #API_HASH
  BOT_TOKEN = os.getenv("BOT_TOKEN", None) # Your Bot Api Token
  OWNER_ID = os.getenv("OWNER_ID")
