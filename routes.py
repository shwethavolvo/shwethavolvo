# routes.py

# Python script, created by Katarina Larsson

from flask import Flask, request

signal_interpreter_app = Flask(__name__)


@signal_interpreter_app.route("/", methods=["GET"])
def hello():
    return "Hello world! says Katarina"


@signal_interpreter_app.route("/", methods=["POST"])
def mirror_data():
    data = request.get_json()
    return data


