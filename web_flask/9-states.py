#!/usr/bin/python3
"""flask"""
from flask import Flask, render_template
from models import storage
import os


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """f ..state- f..state.id"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown(exception):
    """closes"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
