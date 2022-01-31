#!/usr/bin/python3
"""
Runs Flash Application
"""
from models import storage
from models.state import State
from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """
    diplays Python route
    """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ returns an integer """
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ display html page """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ return html """
    if type(n) is int:
        return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """displays html plage"""
    data = storage.all(State).values()
    return render_template('7-states_list.html', data=data)


@app.route('/cities_by_states', strict_slashes=False)
def city_list():
    """displays html plage"""
    data = storage.all(State).values()
    return render_template('8-cities_by_states.html', data=data)


@app.teardown_appcontext
def teardown_data(self):
    """ remove current SQLAlchemy Session """
    return storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
