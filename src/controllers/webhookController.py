from flask import request, jsonify
from services.messageHandler import *

def handleIncoming():
  # Recibe datos de telegram en JSON
  data = request.json
  # Mensaje de usuario
  message = data["message"]["text"]

  handleIncomingMessage(message)
  return jsonify({"status": "success", "message": "Webhook recibido"}), 200