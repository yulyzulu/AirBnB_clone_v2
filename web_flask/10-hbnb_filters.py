#!/usr/bin/python3
"""Script that start a Flash web aplication"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def delete_SQLA(self):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def display_HTML(id=None):
    states = storage.all('State')
    return render_template('10-hbnb_filters.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
