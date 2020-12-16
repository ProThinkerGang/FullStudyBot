
import logging
from pyrogram import filters
from pyrogram import Client

logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.command("/start"))
async def startmsg(client,message):
  await message.reply_text("Hi")
