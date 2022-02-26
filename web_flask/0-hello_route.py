#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask
app = Flask('app')


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """ prints message"""
    return "Hello HBNB!"


if __name__ == '__main__':
    """running app"""
    app.run(host='0.0.0.0', port='5000')
