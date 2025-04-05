from dotenv import load_dotenv
import os

# Cargando variables de entorno
load_dotenv()

# Definiendo variables de entorno
NGROK_AUTHTOKEN = os.getenv("NGROK_AUTHTOKEN")
TELEGRAM_KEY = os.getenv("TELEGRAM_KEY")
BASE_TEL_URL = os.getenv("BASE_TEL_URL")
PORT_DEEPSEEK = os.getenv("PORT_DEEPSEEK")