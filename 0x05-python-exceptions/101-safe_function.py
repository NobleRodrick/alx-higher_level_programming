#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        number = fct(*args)
        return number
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
