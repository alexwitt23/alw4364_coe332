#!/usr/bin/env python3
"""Simple script to read a json created by ``generate_animals.py."""

import json
import pathlib
import random


def print_random_animal(animals_json: pathlib.Path) -> None:
    """Take a path to a json of random animal dictionaries and print one
    at random. """
    animal_data = json.loads(animals_json.read_text())
    assert "animals" in animal_data, f"No 'animals' key in {animals_json}!"
    print(random.choice(animal_data["animals"]))


if __name__ == "__main__":

    animal_json = pathlib.Path(__file__).parent / "animals.json"
    assert (
        animal_json.is_file()
    ), f"Can't find {animal_json}. Please call generate_animals.py first!"

    print_random_animal(animal_json)
