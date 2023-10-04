#!/usr/bin/python3
# 6-print_comb3.py

"""a program that prints all possible different combinations of two digits"""
    for i in range(0, 10):
        for j in range(i + 1, 10):
            if i == 8 and j == 9:
                print("{}{}".format(i, j))
            else:
                print("{}{}".format(i, j), end=", ")

