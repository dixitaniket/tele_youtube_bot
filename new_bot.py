
from telegram.ext import Updater
from telegram.ext import CommandHandler,MessageHandler
from telegram.ext.filters import Filters
from downloader import internal_youtube_routine
import os
# import sqlite3

# conn=sqlite3.connect("userList.db")
updater =Updater(token="",use_context=True,workers=2)

dispatcher=updater.dispatcher

def start(update,context):
    print(update.message)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Welcome to Youtube downloader")

def internal_download(update,context):
    # print(update.text)
    username=update.message.from_user.first_name
    if (update.message.via_bot!=None):
        context.bot.send_message(chat_id=update.effective_chat.id,text="we Do not need music")
    else:
        endpoint=update.message.text
        if (type(endpoint)==type("")):
            filename=internal_youtube_routine(endpoint)
            if filename==False:
                context.bot.send_message(update.message.chat_id,f"some error occured {username}")
           
            try:
                audio = open(filename,"rb")
                
                context.bot.send_message(update.message.chat_id,f"Task in Progress {username}")
                context.bot.send_audio(update.message.chat_id,audio)
                context.bot.send_message(update.message.chat_id,f"Task Completed {username}")
                audio.close()            
                os.remove(filename)
            except Exception as e:
                context.bot.send_message(update.message.chat_id,f"Some error occured {username}")
        else:
            context.bot.send_message(update.message.chat_id,f"Some error occured {username}")




start_handler= CommandHandler("start",start)
message_handler=MessageHandler(Filters.entity("url"),internal_download,run_async=True)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)


updater.start_polling(poll_interval=0.5,read_latency=0.5)

