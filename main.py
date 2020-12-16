import logging
import asyncio as ae
from telethon.sync import TelegramClient
from telethon import events
from Var import var

logging.basicconfig(level=logging.INFO)
studybot = TelegramClient("Study Bot",api_id=var.API_ID,api_hash=var.API_HASH).start(bot_token=var.BOT_TOKEN)

@studybot.on(events.NewMessage)
async def startmessage(event):
    await event.reply("Hi, I am Working")
    
    
with studybot:
    studybot.run_until_disconnected()
