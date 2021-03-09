#!/usr/bin/env python3
"""A collection of various requests that can be made to the API defined in
homework03/app.py."""

import requests


if __name__ == "__main__":

    url = "http://0.0.0.0:5000"
    # Generate animals if they do not already exist.
    response = requests.get(f"{url}/create_animals?path=/tmp/animals.json&number=5")
    response = requests.get(f"{url}/animals")
    response = requests.get(f"{url}/animals?head=lion")
    response = requests.get(f"{url}/animals?head=lion&legs=10")
