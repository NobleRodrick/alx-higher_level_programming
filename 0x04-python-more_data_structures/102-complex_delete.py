#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """deletes keys with specific value in dictionary"""
    the_keys = list(a_dictionary.keys())

    for precise in the_keys:
        if value == a_dictionary.get(precise_value):
            del a_dictionary[precise_value]

    return (a_dictionary)
