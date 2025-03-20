from flask import Flask, request, jsonify
import ngrok
from config import env

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json 
    print("Datos recibidos:", data)  
    return jsonify({"status": "success", "message": "Webhook recibido"}), 200

def set_ngrok():
    listener = ngrok.forward(5000, authtoken = env.NGROK_AUTHTOKEN)
    print(f"Ngrok configurado")
    print(f"url: {listener.url()}")

def main():
    set_ngrok()
    app.run(port = 5000)

if __name__ == '__main__':
    main()