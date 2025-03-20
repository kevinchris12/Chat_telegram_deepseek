from flask import request, jsonify
from services.messageHandler import *

def handleIncoming():
  data = request.json  # Recibe datos en JSON
  print("Datos recibidos:", data)  
  return jsonify({"status": "success", "message": "Webhook recibido"}), 200