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
    if validate_path(path) and path != "":
            return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")

def validate_path(path):
    safe_path = os.path.normpath(path)
    full_path = os.path.join(app.static_folder, safe_path)
    common_path = os.path.commonpath([full_path, app.static_folder])
    return common_path == os.path.abspath(app.static_folder) and \
           os.path.exists(full_path)

if __name__ == "__main__":
    app.run()
