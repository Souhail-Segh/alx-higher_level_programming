#!/usr/bin/python3
"""Defines a function that read text from a file."""


def append_write(filename="", text=""):
    """Print the contents of a text file with UTF8 encoding."""
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
