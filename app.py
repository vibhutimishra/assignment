from flask import Flask,jsonify
import requests

import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

if __name__ == '__main__':
    port = int(os.environ.get('MYAPP_PORT', 8082))

    app.run(host='0.0.0.0', port=port)
