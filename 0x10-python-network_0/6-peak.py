#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    The function in question
    Args:
        list_of_integers(int): a list data type that
        precises the integers to be evaluated
    Returns: the peak of the list or None if not found
    """
    list_size = len(list_of_integers)
    list_middle = list_size
    mid = list_size // 2

    if list_size == 0:
        return None

    while True:
        list_middle = list_middle // 2
        if (mid < list_size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if list_middle // 2 == 0:
                list_middle = 2
            mid = mid + list_middle // 2
        elif list_middle > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if list_middle // 2 == 0:
                list_middle = 2
            mid = mid - list_middle // 2
        else:
            return list_of_integers[mid]
