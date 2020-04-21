#!/usr/bin/python3
"""Script that start a Flash web aplication with two routes"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    """Method that in the route "/" display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display1():
    """Method that in the route "/hbnb" display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display2(text):
    """Method that in the route "/c/<text>" display C text"""
    text1 = text.replace("_", " ")
    return 'C {}'.format(text1)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display3(text='is cool'):
    """Method that in the route "/python/<text>" display
        Python text or Python is cool"""
    return 'Python {}'.format(text.replace("_", " "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
