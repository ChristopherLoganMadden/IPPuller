#Imports
import meth
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():

   return render_template('temp.html')


if __name__ == '__main__':
    app.run()
