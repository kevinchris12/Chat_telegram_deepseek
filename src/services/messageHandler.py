from services.telegramService import *
from services.deepseekService import *
from config import env

deepseekChat = DeepSeekChat(port = env.PORT_DEEPSEEK)

def handleIncomingMessage(chat_id, message_user):
  print("Mensaje usuario:", message_user)
  respuesta = deepseekChat.chat(message_user)
  sendMessage(chat_id, respuesta)