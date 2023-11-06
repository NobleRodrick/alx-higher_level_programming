#!/usr/bin/python3
"""Defines a function that checks whether a class is inherited or not"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): Our defined object.
        a_class (type): We will match the type of the object to this.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
