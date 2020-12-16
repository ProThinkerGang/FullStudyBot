import logging
import asyncio as ae
from telethon.sync import TelegramClient
from telethon import events
from Var import var
from strings import START_STRING

logging.basicConfig(level=logging.INFO)
studybot = TelegramClient("Study Bot",api_id=var.API_ID,api_hash=var.API_HASH).start(bot_token=var.BOT_TOKEN)

@studybot.on(events.NewMessage(pattern="/start" or "/Start" or "/START"))
async def startmessage(event):
    await event.reply(START_STRING)
    
    
with studybot:
    studybot.run_until_disconnected()
