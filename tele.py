import telebot

bot =telebot.TeleBot("1407230169:AAHmqDu4wCjp6Cl46Ipo_8l6qKobUOXr5z0", parse_mode=None)

@bot.message_handler(commands=["start"])
def send_message(message):
    #message.chat.id for the chat id
    bot.reply_to(message,"welcome to mybot, please enter the url of the youtube music video")
    #chat_id=message.chat.id
    
    #audio=open("/home/aniket/Music/Lil Nas X - Panini (Official Video).webm","rb")
    #1bot.send_audio(chat_id,audio)



@bot.message_handler(comamnds=["sendmusic"])
def sending_audio_testing(message):
    bot.reply_to()
    chat_id=message.chat.id
    audio=open("/home/aniket/Music/Lil Nas X - Panini (Official Video).webm","rb")
    bot.send_audio(chat_id,audio)
    

bot.polling()
