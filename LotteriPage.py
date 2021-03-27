from flask import Flask
from Lotteri import Lotteri
from time import sleep
lotto = Lotteri()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "herro"