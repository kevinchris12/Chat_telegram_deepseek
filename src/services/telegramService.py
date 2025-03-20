import requests
from config import env

# Conecta el webhook con la API de Telegram
def webhookUpdates(ngrok_url):
  WEBHOOK_URL = f"{ngrok_url}/webhook"
  url = f"{env.BASE_TEL_URL}{env.TELEGRAM_KEY}/setWebhook"
  params = {"url": WEBHOOK_URL}

  try:
    requests.post(url, params=params)
  except Exception as error:
    print(f"Error en la API de Telegram: {error}")

# Manda mensaje de texto a un chat de Telegram
def sendMessage(chat_id):
  url = f"{env.BASE_TEL_URL}{env.TELEGRAM_KEY}/sendMessage"
  params = {"chat_id": chat_id, "text": "Hola, te mande un mensaje"}

  try:
    requests.post(url, params=params)
  except Exception as error:
    print(f"Error en la API de Telegram: {error}")