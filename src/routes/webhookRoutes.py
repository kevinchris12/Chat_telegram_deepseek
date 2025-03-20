from flask import Blueprint
from controllers.webhookController import *

webhook_bp = Blueprint("webhook", __name__)

webhook_bp.route("/webhook", methods=["POST"])(handleIncoming)