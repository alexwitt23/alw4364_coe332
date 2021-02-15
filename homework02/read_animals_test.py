#!/usr/bin/env python3
"""Simple unittests to ensure homework is correct."""

__author__ = "Alex Witt <awitt2399@utexas.edu>"

import json
import pathlib
import tempfile
from typing import Dict, Union
import unittest

from homework02 import generate_animals
from homework02 import read_animals


class TestReadAnimals(unittest.TestCase):
    def test_no_file_found(self) -> None:
        """Make sure there is an error if the `animals.json` file from
        `generate_animals.py` must exist."""

        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_dir = pathlib.Path(tmp_dir)
            with self.assertRaises(FileNotFoundError):
                read_animals.main(tmp_dir / "animals.json")

    def test_animal_choosen(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_dir = pathlib.Path(tmp_dir)
            animal_json = tmp_dir / "animals.json"
            generate_animals.main(animal_json)
            animal = read_animals.choose_random_animal(animal_json)

            self.assertTrue(isinstance(animal, dict))


class TestChildGeneration(unittest.TestCase):
    def _generate_child(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_dir = pathlib.Path(tmp_dir)
            animal_json = tmp_dir / "animals.json"
            generate_animals.main(animal_json)
            animal_data = json.loads(animal_json.read_text())
            child, parent_a, parent_b = read_animals.breed_animal(
                read_animals.choose_random_animal(animal_json),
                read_animals.choose_random_animal(animal_json),
            )
        return child, parent_a, parent_b

    def test_valid_child_type(self) -> None:
        child, parent_a, parent_b = self._generate_child()
        self.assertTrue(isinstance(child, dict))
        self.assertTrue(isinstance(parent_a, dict))
        self.assertTrue(isinstance(parent_b, dict))

    def test_valid_child_head(self) -> None:
        child, parent_a, parent_b = self._generate_child()
        self.assertIn(child["head"], [parent_a["head"], parent_b["head"]])

    def test_valid_child_arms(self) -> None:
        child, parent_a, parent_b = self._generate_child()
        self.assertIn(child["arms"], [parent_a["arms"], parent_b["arms"]])

    def test_valid_child_legs(self) -> None:
        child, parent_a, parent_b = self._generate_child()
        self.assertIn(child["legs"], [parent_a["legs"], parent_b["legs"]])

    def test_valid_child_tails(self) -> None:
        child, parent_a, parent_b = self._generate_child()
        self.assertIn(child["tails"], [parent_a["tails"], parent_b["tails"]])

    def test_valid_child_body(self) -> None:
        child, parent_a, parent_b = self._generate_child()
        child_body = child["body"].split("-")
        parent_bodies = parent_a["body"].split("-") + parent_b["body"].split("-")

        for child_body_part in child_body:
            self.assertIn(child_body_part, parent_bodies)


if __name__ == "__main__":
    unittest.main()
