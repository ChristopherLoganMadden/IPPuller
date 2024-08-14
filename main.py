#Imports

from flask import Flask
from requests import get



app = Flask(__name__)

@app.route('/')



def index():
    ip =get('https://api.ipify.org?format=js').text
    return "Public IP is " + ip


if __name__ == '__main__':
    app.run()