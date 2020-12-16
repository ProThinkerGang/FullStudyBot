import logging
import asyncio as ae
from telethon.sync import TelegramClient
from telethon import events
from Var import var
from strings import strings
from helpers import stored

logging.basicConfig(level=logging.INFO)
studybot = TelegramClient("Study Bot",api_id=var.API_ID,api_hash=var.API_HASH).start(bot_token=var.BOT_TOKEN)

@studybot.on(events.NewMessage(pattern="/start" or "/Start" or "/START"))
async def startmessage(event):
    await studybot.send_message(event.chat_id,strings.START_STRING,file=stored.START_PIC)
    
    
with studybot:
    studybot.run_until_disconnected()
