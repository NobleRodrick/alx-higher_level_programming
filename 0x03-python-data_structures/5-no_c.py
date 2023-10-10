#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """Eliminates the characters c and C from given string"""
    clone = [a for a in my_string if a != 'c' and a != 'C']
        return ("".join(clone))
