#!/usr/bin/python3
"""will define an object attribute's lookup function location"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
