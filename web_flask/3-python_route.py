#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns Hello HBNB!"""
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB"""
    return('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def CText(text):
    """ returns C followed by text"""
    return("C " + text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>', strict_slashes=False)
def PythonText(text="is cool"):
    """ returns Python followed by text or "is cool" as default """
    return("Python " + text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
