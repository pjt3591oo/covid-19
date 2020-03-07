import os

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '')
CHAT_ID = os.environ.get('CHAT_ID', '')

if not TELEGRAM_TOKEN or not CHAT_ID:
  raise Exception('TELEGRAM_TOKEN, CHAT_ID 확인필요')

if __name__ == "__main__":
  print(TELEGRAM_TOKEN)
  print(CHAT_ID)