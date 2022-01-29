#!/usr/bin/python3
"""
Flask application
Routes:
    * /: display "Hello HBNB!"
    * /hbnb: display "HBNB"
    * /c/<text>: display “C ” followed by the value of the
        text variable (replace underscore _ symbols with a space)
"""

from flask import Flask, escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ prints message"""
    return 'Hello HBNB!'


@app.route('/', strict_slashes=False)
def hbnb_route():
    """
    display Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    diplays C
    """
    return 'C %s' % escape(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
