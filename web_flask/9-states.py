#!/usr/bin/python3
"""flask"""
from flask import Flask, render_template
from models import storage
import os


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """tearup"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ f...f """
    missin = False
    if id is not None:
        states = storage.all(State, id)
        id_pls = True
        if len(states) == 0:
            missin = True
    else:
        states = storage.all(State)
        id_pls = False
    return render_template(
            '9-states.html', states=states, with_id=id_pls,
            not_found=missin)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
