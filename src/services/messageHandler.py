from services.telegramService import *

def handleIncomingMessage(chat_id, message):
  print("Mensaje recibido:", message)
  sendMessage(chat_id)