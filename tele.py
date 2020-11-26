import telebot
from downloader import internal_youtube_routine
import os

bot =telebot.TeleBot("1407230169:AAHmqDu4wCjp6Cl46Ipo_8l6qKobUOXr5z0", parse_mode=None)


@bot.message_handler(commands=["start"])
def send_message(message):
    #message.chat.id for the chat id
    bot.reply_to(message,"welcome to mybot, please enter the url of the youtube music video")
    chat_id=message.chat.id
    print(chat_id)
    bot.reply_to(message,"hello")
    #audio=open("/home/aniket/Music/Dylan Sitts - So Free.webm","rb")

    #bot.send_audio(chat_id,audio)



@bot.message_handler(commands=["sendmusic"])
def sending_audio_testing(message):   	
    bot.reply_to(message,"paste in the youtube url")


@bot.message_handler(commands=["future"])
def internal_future(message):
    bot.reply_to(message,"currently working on downloading videos directly from youtube to your chat")

@bot.message_handler(commands=["about"])
def internal_about(message):
    bot.reply_to("bot made by someone you know")

def url_checker(message):
    if (message.entities==None):
        return False
    else:
        if (message.entities[0].type=="url"):
            return True
        else:
            return False


    
@bot.message_handler(func=url_checker)
def internal_url_handler(message):
    print(message.entities[0].type)
    try:
        bot.reply_to(message,"sending audio to chat")
        filename=internal_youtube_routine(message.text)
        if (filename==False):
            bot.reply_to(message,"sorry some error occured while downloading")
        else:
            audio=open(filename,"rb")
            bot.send_audio(message.chat.id,audio)
            bot.reply_to(message,"delivered boss")
            audio.close()
            os.remove(filename)
    except Exception as e:
        print(e)
        bot.reply_to(message,"shit")

import time
while True:
    try:
        bot.polling(none_stop=True,timeout=200)
    except Exception as e:
        print(e)
        time.sleep(10)
