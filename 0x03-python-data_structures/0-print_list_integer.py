#!/usr/bin/python3
# 0-print_list_integer.py


def print_list_integer(my_list=[]):
    """function prints the integers found in a LIST"""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
