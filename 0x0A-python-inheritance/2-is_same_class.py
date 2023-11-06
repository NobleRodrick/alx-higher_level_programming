#!/usr/bin/python3
"""Defines a function that checks a class"""


def is_same_class(obj, a_class):
    """Check whether an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the obj type.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
