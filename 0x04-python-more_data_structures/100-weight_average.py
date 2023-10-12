#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integer tuples"""
    if not my_list:
        return 0

    number = 0
    denominator = 0

    for tupl in my_list:
        number += tupl[0] * tupl[1]
        denominator += tupl[1]

    return (number / denominator)
