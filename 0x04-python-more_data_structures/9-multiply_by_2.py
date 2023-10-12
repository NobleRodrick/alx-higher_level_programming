#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """returns new dictionary with values mmultiplied by 2"""
    new_dictionary = a_dictionary.copy()
    dic_keys = list(new_dictionary.keys())

    for i in dic_keys:
        new_dictionary[i] *= 2

    return (new_dictionary)
