from flask import Flask, request, jsonify
import logging, sys

app = Flask(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
app.logger.setLevel(logging.INFO)

@app.route('/')
def home():
    return "Flask Login Monitor App is running"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username, password = data.get('username'), data.get('password')
    if username == 'admin' and password == 'password123':
        app.logger.info(f"Successful login attempt for user: {username}")
        return jsonify({"message": "Login successful!"}), 200
    else:
        app.logger.warning(f"Failed login attempt for user: {username}")
        return jsonify({"message": "Login failed!"}), 401
