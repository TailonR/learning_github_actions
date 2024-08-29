#!/usr/bin/env python3
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder="build")
CORS(app)

@app.route("/hello")
def hello_world():
    return jsonify({"data": "Hello, I know a little more now!\n"})


if __name__ == "__main__":
    app.run()
