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

app.run(host='0.0.0.0', port=5000)
