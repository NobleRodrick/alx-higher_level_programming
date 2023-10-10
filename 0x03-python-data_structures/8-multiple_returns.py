#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(sentence):
    """gives the first character and length of a string."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
