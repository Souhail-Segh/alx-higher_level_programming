#!/usr/bin/python3
"""Defines a json file-reading function."""
import json


def load_from_json_file(filename):
    """Read an object to a text file using json representation."""
    with open(filename, "r") as f:
        return(json.load(f))
