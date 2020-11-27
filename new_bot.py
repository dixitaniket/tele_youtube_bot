# 1407230169:AAHmqDu4wCjp6Cl46Ipo_8l6qKobUOXr5z0
from telegram.ext import Updater
from telegram.ext import CommandHandler,MessageHandler
from telegram.ext.filters import Filters
from downloader import internal_youtube_routine
import os

updater =Updater(token="1407230169:AAHmqDu4wCjp6Cl46Ipo_8l6qKobUOXr5z0",use_context=True)

dispatcher=updater.dispatcher

def start(update,context):
    print(update.message)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Welcome to Youtube downloader")

def internal_download(update,context):
    # print(update.text)
    if (update.message.via_bot!=None):
        context.bot.send_message(chat_id=update.effective_chat.id,text="we Do not need music")
    else:
        endpoint=update.message.text
        if (type(endpoint)==type("")):
            filename=internal_youtube_routine(endpoint)
            if filename==False:
                context.bot.send_message(update.message.chat_id,"some error occured")
            audio = open(filename,"rb")
            context.bot.send_audio(update.message.chat_id,audio)
            context.bot.send_message (update.message.chat_id,"task complete")
            audio.close()            
            os.remove(filename)
        else:
            context.bot.send_message(update.message.chat_id,"some error occured")




start_handler= CommandHandler("start",start)
message_handler=MessageHandler(Filters.entity("url"),internal_download)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()

