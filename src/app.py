from dotenv import load_dotenv
import os
from flask import Flask, request, render_template
import datetime
from routes.chatbot_routes import chatbot_bp


# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.register_blueprint(chatbot_bp)

def log_event(event_type, client_ip, details=""):
    with open('logs\\log.txt', 'a') as log_file:
        log_file.write(f"{datetime.datetime.now()} - {event_type} - {client_ip} - {details}\n")

@app.before_request
def log_request():
    details = (
        f"Method: {request.method}, "
        f"URL: {request.url}, "
        f"Headers: {dict(request.headers)}, "
        f"Form Data: {request.form}, "
        f"JSON Payload: {request.get_json(silent=True)}"
    )
    log_event('Request', request.remote_addr, details)

@app.route('/join')
def join():
    log_event('Join', request.remote_addr)
    return "Client joined"

@app.route('/leave')
def leave():
    log_event('Leave', request.remote_addr)
    return "Client left"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)