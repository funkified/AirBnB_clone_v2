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
    """ display Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    diplays HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    diplays C
    """
    return 'C %s' % replace.text('_', ' ')


@app.route('/python')
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is_cool'):
    """
    diplays Python route
    """
    return 'Python %s' % text.replace('_', ' ')


if __name__ == '__main__':
    """ run Flask app """
    app.run(host='0.0.0.0', port=5000)
