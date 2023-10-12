#!/usr/bin/python3
def number_keys(a_dictionary):
    """Gives the number of keys found in a dictionary"""
    tot = 0
    the_keys = list(a_dictionary.keys())

    for i in the_keys:
        tot += 1

    return (tot)
