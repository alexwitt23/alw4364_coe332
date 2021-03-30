"""This Flask app exposes a REST API which reads animal information from a
Redis database."""

import datetime
import json
import os

import flask
from flask import request
from flask import jsonify
import redis

from midterm import generate_animals

app = flask.Flask(__name__)
rd = redis.StrictRedis(
    host="redis", port=6379, db=0, charset="utf-8", decode_responses=True
)


@app.route("/create_animals", methods=["GET"])
def create_animals():
    """Generate animals and populate a redis database. The function expects the
    user to pass `number=foo`"""
    num_animals = request.args.get("number", default=1, type=int)
    for _ in range(num_animals):
        animal = generate_animals.generate_animal()
        rd.set(animal["uuid"], json.dumps(animal))

    return jsonify({key: rd.get(key) for key in rd.keys("*")})


@app.route("/get_date_range", methods=["GET"])
def get_date_range():
    """Specify a start and end date and get animals that fall within the
    range. YYYY-MM-DDTHH:HH:SS.MS """
    start_date = request.args.get("start", default=None, type=str)
    start_date = datetime.datetime.fromisoformat(start_date)
    end_date = request.args.get("end", default=None, type=str)
    end_date = datetime.datetime.fromisoformat(end_date)

    animals = []
    for key in rd.keys("*"):
        animal = json.loads(rd.get(key))
        if (
            start_date
            <= datetime.datetime.fromisoformat(animal["created-on"])
            <= end_date
        ):
            animals.append(animal)

    return jsonify(animals)


@app.route("/get_uuid", methods=["GET"])
def get_uuid():
    """Get animal based on uuid specifier."""
    animal_uuid = request.args.get("uuid", default=1, type=str)
    return jsonify(rd.get(animal_uuid))


@app.route("/update_animal", methods=["GET"])
def update_animal():
    """Edit an existing animal.

    Specify an animal to edit by uuid. Then pass any of the follow animal
    parameters with values to update: body, arms, legs, tails."""

    animal_uuid = request.args.get("uuid", default=None, type=str)
    animal = json.loads(rd.get(animal_uuid))

    new_animal_body = request.args.get("body", default=None, type=str)
    if new_animal_body is not None:
        animal["body"] = new_animal_body

    new_animal_arms = request.args.get("arms", default=None, type=int)
    if new_animal_body is not None:
        animal["arms"] = new_animal_arms

    new_animal_legs = request.args.get("legs", default=None, type=int)
    if new_animal_legs is not None:
        animal["legs"] = new_animal_legs

    new_animal_tails = request.args.get("tails", default=None, type=int)
    if new_animal_tails is not None:
        animal["tails"] = new_animal_tails

    rd.set(animal_uuid, json.dumps(animal))
    return animal


@app.route("/remove_by_date", methods=["GET"])
def remove_by_date():
    """Specify a start and end date and remove all animals that fall within the
    range. YYYY-MM-DDTHH:HH:SS.MS """
    start_date = request.args.get("start", default=None, type=str)
    start_date = datetime.datetime.fromisoformat(start_date)
    end_date = request.args.get("end", default=None, type=str)
    end_date = datetime.datetime.fromisoformat(end_date)

    removed = []
    for key in rd.keys("*"):
        animal = json.loads(rd.get(key))
        if (
            start_date
            <= datetime.datetime.fromisoformat(animal["created-on"])
            <= end_date
        ):
            removed.append(animal)

    for animal in removed:
        rd.delete(animal["uuid"])

    return jsonify(removed)


@app.route("/get_leg_average", methods=["GET"])
def get_leg_average():
    """Get the average number of legs across all the animals in 
    the dataset."""
    animals = [json.loads(rd.get(key)) for key in rd.keys("*")]
    legs = [animal["legs"] for animal in animals]
    return jsonify(sum(legs) / len(legs))


@app.route("/get_num_animals", methods=["GET"])
def get_num_animals():
    """Get the total number of animals in the dataset."""
    return jsonify(len(list(rd.keys("*"))))


@app.route("/get_animals", methods=["GET"])
def get_animals():
    """Print out all the animals in the dataset."""
    return jsonify({key: rd.get(key) for key in rd.keys("*")})


if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0")
