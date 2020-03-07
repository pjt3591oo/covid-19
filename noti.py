from config import TELEGRAM_TOKEN, CHAT_ID
import requests as rq
import telegram 

bot = telegram.Bot(token=TELEGRAM_TOKEN)

def send(t):
  bot.sendMessage(CHAT_ID, t, parse_mode=telegram.ParseMode.HTML)
  # rq.post('https://api.telegram.org/bot1074246557:AAE6O2Okcd4RyJ2jN26RYv9uxI6sRi-UpVc/sendMessage?chat_id=%s&text=%s'%(chat_id, t))