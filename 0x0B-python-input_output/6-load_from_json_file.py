#!/usr/bin/python3
"""Defines a json file-reading function."""
import json


def save_to_json_file(my_obj, filename):
    """Read an object to a text file using json representation."""
    with open(filename, "r") as f:
        json.load(f)
