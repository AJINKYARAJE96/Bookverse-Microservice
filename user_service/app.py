# BookVerse Microservices - Flask + Docker + AWS Ready

# Each microservice will be in its own folder with a Dockerfile.
# This is a simplified structure and starter code.

# ------------------------------------------
# user_service/app.py
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user_id = str(uuid.uuid4())
    users[user_id] = {
        "username": data['username'],
        "password": data['password']  # Not secure, use hashing in prod
    }
    return jsonify({"user_id": user_id}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    for uid, user in users.items():
        if user['username'] == data['username'] and user['password'] == data['password']:
            return jsonify({"message": "Login successful", "user_id": uid})
    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
