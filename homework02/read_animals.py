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


def breed_animal(
    parent_a: Dict[str, Union[int, str]], parent_b: Dict[str, Union[int, str]]
) -> Dict[str, Union[int, str]]:
    """Take in two animal dictionaries and generate a child."""
    # Take a random head from a parent.
    child = {}
    for key in ["head", "arms", "legs", "tails"]:
        child[key] = random.choice([parent_a[key], parent_b[key]])
    # Since each parent body is a combination of two animals, get two random parts
    # from the four possible.
    child["body"] = "-".join(
        random.sample(parent_a["body"].split("-") + parent_b["body"].split("-"), 2)
    )
    return child, parent_a, parent_b


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

    child, parent_a, parent_b = breed_animal(
        choose_random_animal(animals_json_path), choose_random_animal(animals_json_path)
    )
    print("Two random animals have created a child!")
    print(f"Parent A: {parent_a}\nParent B: {parent_b}")
    print(f"Child: {child}")


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
