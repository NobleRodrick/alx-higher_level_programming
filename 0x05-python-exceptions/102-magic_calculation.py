#!/usr/bin/python3
"""replicating what bytecode does"""
def magic_calculation(a, b):
    rslut = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                rsult += a ** b / i
        except Exception:
            rsult = b + a
            break
    return rsult
