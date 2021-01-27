#!/usr/bin/env python3
"""Simple script to write a json of random Dr. Moreau-esk animals to a json file."""

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


if __name__ == "__main__":
    animals = {"animals": []}
    for _ in range(20):
        animals["animals"].append(generate_animal())

    pathlib.Path("animals.json").write_text(json.dumps(animals, indent=2))
