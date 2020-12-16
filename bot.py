from pyrogram import Client
from Var import var
import logging

logging.basicConfig(level=logging.INFO)
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


if __name__=="__main__":
  studybot= Client("Full Study Bot",
                  api_id=var.API_ID,
                 api_hash=var.API_HASH,
                 bot_token=var.BOT_API_TOKEN,
                 plugins=plugins)
  studybot.run()
