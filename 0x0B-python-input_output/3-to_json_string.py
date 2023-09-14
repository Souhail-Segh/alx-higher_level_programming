#!/usr/bin/python3
"""Defines a to_jsson_string function."""
import json


def to_json_string(my_obj):
    """Return JSON representation in a string object."""
    return json.dumps(my_obj)
