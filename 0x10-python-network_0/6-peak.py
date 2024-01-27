#!/usr/bin/python3
"""
Finds that peak in a list of unsorted integers
"""


def find_peak(defined_integer_list):
    """
    Return a peak in a list of unsorted integers.
    """
    if defined_integer_list == []:
        return None

    size = len(defined_integer_list)
    if size == 1:
        return defined_integer_list[0]
    elif size == 2:
        return max(defined_integer_list)

    mid = int(size / 2)
    peak = defined_integer_list[mid]
    if peak > defined_integer_list[mid - 1] and peak > defined_integer_list[mid + 1]:
        return peak
    elif peak < defined_integer_list[mid - 1]:
        return find_peak(defined_integer_list[:mid])
    else:
        return find_peak(defined_integer_list[mid + 1:])
