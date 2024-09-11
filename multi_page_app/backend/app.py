#!/usr/bin/env python3
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="../frontend/build", static_url_path="")
CORS(app)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if is_allowed(path):
        if path != "":
            return send_from_directory(app.static_folder, path)
        else:
            return send_from_directory(app.static_folder, "index.html")
    return send_from_directory(app.static_folder, "index.html")

def is_allowed(path):
    with open("backend/whitelist.txt", "r") as file:
        lines = file.read().splitlines()
        print(lines)
        print(path in lines)
        return path in lines

if __name__ == "__main__":
    app.run()
