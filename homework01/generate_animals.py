#!/usr/bin/env python3
"""Simple script to write a json of random Dr. Moreau-esk animals to a json file."""

__author__ = "Alex Witt <awitt2399@utexas.edu>"

import json
import pathlib
import random
from typing import Dict, Union

import petname

_HEADS = ["snake", "bull", "lion", "raven", "bunny"]


def generate_animal() -> Dict[str, Union[int, str]]:
    """Generate a random animal.

    Returns:
        A dictionary of the random animal's attributes.
    """
    animal = {"head": random.choice(_HEADS)}
    animal["body"] = f"{petname.Generate(1, '')}-{petname.Generate(1, '')}"
    animal["arms"] = random.choice(range(2, 11, 2))
    animal["legs"] = random.choice(range(3, 13, 3))
    animal["tails"] = animal["arms"] + animal["legs"]

    return animal


def main(save_dir: pathlib.Path = pathlib.Path(__file__).parent) -> None:
    """Entrypoint function that generates 20 random animals them writes them to
    a json file."""
    animals = {"animals": []}
    for _ in range(20):
        animals["animals"].append(generate_animal())

    save_path = save_dir / "animals.json"
    save_path.write_text(json.dumps(animals, indent=2))


if __name__ == "__main__":
    main()
