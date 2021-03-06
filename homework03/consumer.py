#!/usr/bin/env python3
"""A collection of various requests that can be made to the API defined in
homework03/app.py."""

import requests


if __name__ == "__main__":

    url = "http://0.0.0.0:5038"
    # Generate animals if they do not already exist.
    response = requests.get(f"{url}/create_animals?path=/tmp/animals.json&number=100")
    response = requests.get(f"{url}/animals")
    print(response.json())
    response = requests.get(f"{url}/animals?head=lion")
    print(response.json())
    response = requests.get(f"{url}/animals?head=lion&legs=10")
    print(response.json())
