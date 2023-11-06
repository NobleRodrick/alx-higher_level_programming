#!/usr/bin/python3
"""Defines an inherited list class to MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """prints a sorted list in ascending order"""
        print(sorted(self))
