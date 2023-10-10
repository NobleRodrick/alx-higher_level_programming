#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """Tells the members if the list that are divisible by 2"""
    mults_two = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mults_two.append(True)
        else:
            mults_two.append(False)

    return (mults_two)
