from pyrogram import Client
from Var import var

studybot = Client(api_id=var.API_ID,
                 api_hash=var.API_HASH,
                 bot_token=var.BOT_API_TOKEN,
                 plugins=dict(root="plugins"))

studybot.run()
