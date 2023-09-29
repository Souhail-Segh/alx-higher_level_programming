#!/usr/bin/python3
"""Defines Python class-dict-JSON function."""


def class_to_json(obj):
    """Return the dict represntation."""
    return obj.__dict__
