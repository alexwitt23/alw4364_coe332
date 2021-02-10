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


if __name__ == "__main__":
    unittest.main()
