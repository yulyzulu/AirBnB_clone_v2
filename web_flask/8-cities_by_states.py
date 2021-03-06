#!/usr/bin/python3
"""Script that start a Flash web aplication"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def delete_SQLA(self):
    """Remove the current SQLAlchemySession"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_HTML():
    """Display a html with states and cities"""
    state = storage.all('State')
    return render_template('8-cities_by_states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
