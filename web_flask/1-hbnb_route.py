#!/usr/bin/python3
""" flask 2 """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ fuinc """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def indextwo():
    """ func2 """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
