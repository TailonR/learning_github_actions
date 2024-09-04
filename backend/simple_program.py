#!/usr/bin/env python3
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="build")
CORS(app)


@app.route("/hello")
def hello_world():
    return jsonify({"data": "Hello, I know a little more now!\n"})


@app.route("/", defaults={"path": ''})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run()
