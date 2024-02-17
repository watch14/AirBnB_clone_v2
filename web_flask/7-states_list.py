#!/usr/bin/python3
""" flasks / """

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ func list """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(error):
    """ fnc err """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
