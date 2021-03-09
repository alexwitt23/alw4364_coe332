#!/usr/bin/env python3

import json
import pathlib
import tempfile
import unittest

from homework03 import app


class CreateAnimals(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_create_animals(self):

        with tempfile.NamedTemporaryFile() as f:
            response = self.app.get(f"/create_animals?path={f.name}")
            f = pathlib.Path(f.name)
            self.assertTrue(f.is_file())

    def _create_animals_num(self, num: int):

        with tempfile.NamedTemporaryFile() as f:
            response = self.app.get(f"/create_animals?path={f.name}&number={num}")
            f = pathlib.Path(f.name)
            self.assertTrue(f.is_file())

            data = json.loads(f.read_text())
            self.assertEqual(num, len(data["animals"]))

        return response

    def test_create_animals_num(self):

        for num in [1, 10, 15, 20, 23, 42, 112]:
            self._create_animals_num(num)

    def test_create_animals_fail(self):
        with tempfile.NamedTemporaryFile() as f:
            response = self.app.get(f"/create_animals?path={f.name}&number=0")
            self.assertEqual(response._status_code, 400)


class GetAnimals(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.animal_json = pathlib.Path(tempfile.NamedTemporaryFile().name)
        self.app.get(f"/create_animals?path={str(self.animal_json)}")
        self.animal_data = json.loads(self.animal_json.read_text())

    def test_get_animals(self):

        response = self.app.get(f"/animals")
        self.assertListEqual(self.animal_data["animals"], response.json)


if __name__ == "__main__":
    unittest.main()
