from flask import Flask
import ngrok
from config import env
from routes.webhookRoutes import webhook_bp

app = Flask(__name__)
app.register_blueprint(webhook_bp)

# Exponiendo puerto
def set_ngrok():
    listener = ngrok.forward(5000, authtoken = env.NGROK_AUTHTOKEN)
    print(f"Ngrok configurado")
    print(f"url: {listener.url()}")

def main():
    set_ngrok()
    app.run(port = 5000)

if __name__ == '__main__':
    main()