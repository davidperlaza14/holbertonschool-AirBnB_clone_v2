#!/usr/bin/python3
"""using flask with storage and db storage"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """show list of states"""
    state = storage.all(State).values()
    return render_template("7-states_list.html", state=state)


@app.teardown_appcontext
def teardown(execption):
    """closing storage"""
    return storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)