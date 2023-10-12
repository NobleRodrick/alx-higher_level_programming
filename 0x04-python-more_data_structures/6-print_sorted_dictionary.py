#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints dictionary by sorted keys"""
    ordered_list = list(a_dictionary.keys())
    ordered_list.sort()
    for i in ordered_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
