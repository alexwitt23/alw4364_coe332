#!/usr/bin/env python3
"""Simple script to read a json created by ``generate_animals.py."""

__author__ = "Alex Witt <awitt2399@utexas.edu>"

import argparse
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


def main(
    animals_json_path: pathlib.Path = pathlib.Path(__file__).parent / "animals.json",
) -> None:
    """Entrypoint function to read a random animal from previously generated
    list of animals."""

    if not animals_json_path.is_file():
        raise FileNotFoundError(
            f"Can't find {animals_json_path}. Please call generate_animals.py first!"
        )

    animal = choose_random_animal(animals_json_path)
    print(animal)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument(
        "--animals_json_path",
        type=pathlib.Path,
        required=False,
        default=pathlib.Path(__file__).parent / "animals.json",
        help="Where to find the generated animals json file.",
    )
    args = parser.parse_args()
    main(animals_json_path=args.animals_json_path.expanduser())
