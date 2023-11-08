#!/usr/bin/python3
"""Defines a function that appends files."""


def append_write(filename="", text=""):
    """Appends string to the end of a UTF-8 text encoded format file

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
