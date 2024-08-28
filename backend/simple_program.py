#!/usr/bin/env python3
from flask import Flask, jsonify

app = Flask(__name__, static_folder='../frontend/public')


@app.route("/hello")
def hello_world():
    return jsonify({'data': "Hello, I know a little more now!\n"})


if __name__ == "__main__":
    app.run()
