#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Gives the sum of uniques in list"""
    uniques = set(my_list)
    tot = 0

    for i in uniques:
        tot += i

    return (tot)
