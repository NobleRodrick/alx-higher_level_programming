#!/usr/bin/python3
# 101-remove_char_at.py


def remove_char_at(str, n):
    """Create a copy of the string while skipping char at nth position"""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])

