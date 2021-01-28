#!/usr/bin/env python3
"""Simple script to read a json created by ``generate_animals.py."""

__author__ = "Alex Witt <awitt2399@utexas.edu>"

import json
import pathlib
import random
from typing import Dict, Union


def choose_random_animal(animals_json: pathlib.Path) -> Dict[str, Union[int, str]]:
    """Take a path to a json of random animal dictionaries and print one
    at random. """
    animal_data = json.loads(animals_json.read_text())
    assert "animals" in animal_data, f"No 'animals' key in {animals_json}!"

    return random.choice(animal_data["animals"])


def main() -> None:
    """Entrypoint function to read a random animal from previously generated
    list of animals."""

    animal_json = pathlib.Path(__file__).parent / "animals.json"
    if not animal_json.is_file():
        raise FileNotFoundError(
            f"Can't find {animal_json}. Please call generate_animals.py first!"
        )

    animal = choose_random_animal(animal_json)
    print(animal)


if __name__ == "__main__":
    main()
