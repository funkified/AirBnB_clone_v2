#!/usr/bin/python3
"""
Flask application
Routes:
    * /: display "Hello HBNB!"
    * /hbnb: display "HBNB"
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ prints message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    diplays HBNB
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
