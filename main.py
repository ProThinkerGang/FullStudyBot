#================================================ # IMPORTS & BASIC SCHEME =========================================================
import logging
import asyncio as ae
from telethon.sync import TelegramClient
from telethon import events
from Var import var
from strings import strings
from helpers import stored

logging.basicConfig(level=logging.INFO)

studybot = TelegramClient("Study Bot",
                          api_id=var.API_ID,
                          api_hash=var.API_HASH
                         ).start(bot_token=var.BOT_TOKEN)

#============================================================== # START  =========================================================

@studybot.on(events.NewMessage(pattern="/start" or "/Start" or "/START"))
async def startmessage(event):
    if event.is_private:
        await studybot.send_message(event.chat_id,
                                strings.START_STRING,
                                file=stored.START_PIC)
    else:
        await studybot.send_message(event.chat_id,
                                   "I Am Alive !")
        
        

#======================================================== # BOT JOINED =========================================================

@studybot.on(events.ChatAction)
async def botadded(e):
    bot = await studybot.get_me()
    botid = bot.id
    if e.is_added:
        if e.user.id == botid:
            await e.reply("Thanks for Adding Me !!")
            
    
#============================================================== # END =========================================================
    
    
    
    
    
with studybot:
    studybot.run_until_disconnected()
