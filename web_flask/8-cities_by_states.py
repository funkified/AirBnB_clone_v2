#!/usr/bin/python3
"""
Runs Flash Application
"""
from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown_data(self):
    """ remove current SQLAlchemy Session """
    return storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def index():
    """displays html plage"""
    data = storage.all('State')
    return render_template('8-cities_by_states.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
