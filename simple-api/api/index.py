from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from your custom API!",
        "status": "success"
    })

@app.route('/about')
def about():
    return jsonify({
        "owner": "You",
        "description": "The simplest API ever."
    })
