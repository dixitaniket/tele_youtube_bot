# Youtube telebot 

> Download audio from youtube video's just by copying and pasting it's link in the telegram

- Clone repo
- pip install requirements.txt / pip3 install requirements.txt (if using a linux distribution or during deployment)
- Generate a bot token from telegram and replace it in token 
```
updater =Updater(token="<your token here>",use_context=True,workers=2)
```
- run the bot file using 
```
python new_bot.py
```
- or if on a linux distribution

```
python3 new_bot.py
```

If deploying on a linux server use screen to keep the file running
> on the terminal in the server use the follwing commands
```
screen 
python3 new_bot.py
ctrl + a + d
```
> the code file will keep running , if you have to reconnect,use the command
```
screen -r
```
