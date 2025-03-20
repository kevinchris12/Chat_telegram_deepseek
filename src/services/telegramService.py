import requests
from config import env

def webhookUpdates(ngrok_url):
  WEBHOOK_URL = f"{ngrok_url}/webhook"
  url = f"{env.BASE_TEL_URL}{env.TELEGRAM_KEY}/setWebhook"
  params = {"url": WEBHOOK_URL}

  try:
    requests.post(url, params=params)
  except Exception as error:
    print(f"Error en la API de Telegram: {error}")