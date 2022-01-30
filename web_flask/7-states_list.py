#!/usr/bin/python3
"""
Runs Flash Application
"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown_data(self):
    """ remove current SQLAlchemy Session """
    return storage.close()


@app.route('/states_list', strict_slashes=False)
def index():
    """displays html plage"""
    data = storage.all(State)
    return render_template('7-states_list.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
