#!/usr/bin/env python3
"""Simple unittests to ensure homework is correct."""

__author__ = "Alex Witt <awitt2399@utexas.edu>"

import json
import pathlib
from typing import Dict, Union
import unittest

from homework02 import generate_animals


class TestGenerateAnimals(unittest.TestCase):

    _animal_parts = ["head", "body", "arms", "legs", "tails"]

    def _check_keys(self, animal: Dict[str, Union[str, int]]) -> bool:
        return self._animal_parts == list(animal.keys())

    def test_animal_parts(self) -> None:
        animal = generate_animals.generate_animal()
        self.assertEqual(self._animal_parts, list(animal.keys()))

    def test_tails(self) -> None:
        """Tail should be the sum of arms and legs."""
        animal = generate_animals.generate_animal()
        self.assertEqual(animal["tails"], animal["arms"] + animal["legs"])

    def test_written_json(self) -> None:
        """A json file should be written in the same folder as
        `generate_animals.py`."""
        generate_animals.main()

        json_path = pathlib.Path(__file__).parent / "animals.json"
        self.assertTrue(json_path.is_file())

    def test_json_contents(self) -> None:
        """A json file should be written in the same folder as
        `generate_animals.py`. It should have twenty animals."""
        generate_animals.main()
        json_path = pathlib.Path(__file__).parent / "animals.json"
        json_data = json.loads(json_path.read_text())

        self.assertEqual(len(json_data["animals"]), 20)

        # Make sure each animal has the proper keys.
        for animal in json_data["animals"]:
            self.assertTrue(self._check_keys(animal))


if __name__ == "__main__":
    unittest.main()
