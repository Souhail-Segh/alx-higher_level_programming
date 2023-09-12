#!/usr/bin/python3
"""Defines a function that read text from a file."""


def read_file(filename=""):
    """Print the contents of a text file with UTF8 encoding."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
