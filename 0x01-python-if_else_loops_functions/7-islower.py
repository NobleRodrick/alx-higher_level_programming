#!/usr/bin/python3
# 7-islower.py

def islower(num):
    if ord(num) >= 97 and ord(num) <= 122:
        return True
    else:
        return False
