#!/usr/bin/python3
"""Defines a function that reads txt files"""


def read_file(filename=""):
    """Print the contents of a UTF-8 text format file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
