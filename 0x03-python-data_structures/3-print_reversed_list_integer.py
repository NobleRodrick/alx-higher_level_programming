#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """reverses a list and prints elements in that order"""
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
