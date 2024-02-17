#!/usr/bin/python3
"""start app"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


@app.teardown_appcontext
def handle_teardown(self):
    """teardow"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ list sates """
    states = storage.all('State').values()
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
