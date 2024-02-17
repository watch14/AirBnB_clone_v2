#!/usr/bin/python3
""" module doc """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown(error):
    """ tearit """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb2():
    """ filter it """
    amenities = storage.all(Amenity)
    states = storage.all(State)
    return render_template(
            '10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
