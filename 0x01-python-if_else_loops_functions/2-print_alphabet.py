#!/usr/bin/python3
# 2-print_alphabet.py

"""We are printing the ASCI alphabet in lwr case, excluding a new line"""
for asci in range(97, 123):
        print("{}".format(chr(asci)), end="")
