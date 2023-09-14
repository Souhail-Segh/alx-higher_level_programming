#!/usr/bin/python3
"""Defines a from_JSON_string function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a json string."""
    return json.loads(my_str)
