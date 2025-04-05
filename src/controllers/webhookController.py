from flask import request, jsonify
from services.messageHandler import *

def handleIncoming():
  # Recibe datos de telegram en JSON
  data = request.json
  # Mensaje de usuario
  message_user = data["message"]["text"]
  # Chat al que pertenece el mensaje
  chat_id = data["message"]["chat"]["id"]

  handleIncomingMessage(chat_id, message_user)
  return jsonify({"status": "success", "message": "Webhook recibido"}), 200