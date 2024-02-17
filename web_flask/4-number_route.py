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


@app.route("/c/<text>", strict_slashes=False)
def indexthree(text):
    """ func3 """
    text = text.replace("_", " ")
    return "C " + f"{text}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def indexfour(text):
    """ func4 """
    return 'Python {}'.format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def indexfive(n):
    """ func5 """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
