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


@app.route('/hbnb_filters', strict_slashes=False)
def display_HTML():
    """Display a html with states, cities and amenities"""
    states = storage.all('State')
    ame = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=states, amenity=ame)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
