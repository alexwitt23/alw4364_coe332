"""
PYTHONPATH=. FLASK_APP=homework3/app.py FLASK_ENV=development python3 homework03/app.py
"""

import pathlib
import json

import flask
from flask import request
from flask import jsonify

from homework02 import generate_animals

app = flask.Flask(__name__)
cache = {"file_path": None}


def read_data():
    return json.loads(pathlib.Path(cache["file_path"]).read_text())


@app.route("/create_animals", methods=["GET"])
def create_animals():
    num_animals = request.args.get("number", default=1, type=int)
    cache["file_path"] = request.args.get("path", default="animals.json", type=str)
    if not num_animals > 0:
        return flask.Response(
            response="number must be greater than 0.", status=400, headers={}
        )

    animals = {"animals": []}
    for _ in range(num_animals):
        animals["animals"].append(generate_animals.generate_animal())

    pathlib.Path(cache["file_path"]).write_text(json.dumps(animals))
    return flask.Response(response="Created animals", status=201, headers={})


@app.route("/animals", methods=["GET"])
def get_animals():
    animals = read_data()["animals"]
    head_type = request.args.get("head", default=None, type=str)
    num_legs = request.args.get("legs", default=None, type=int)

    if head_type is not None:
        animals = [animal for animal in animals if animal["head"] == head_type]

    if num_legs is not None:
        animals = [animal for animal in animals if animal["legs"] == num_legs]

    return jsonify(animals)


if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0")
