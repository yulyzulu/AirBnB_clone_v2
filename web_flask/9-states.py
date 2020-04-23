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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_HTML(id=None):
    """Display a html with states and id cities"""
    states = storage.all('State')
    for state in states.values():
        if state.id == id:
            states = state
    return render_template('9-states.html', states=states, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
