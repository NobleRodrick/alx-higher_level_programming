#!/usr/bin/python3
for item in range(97, 123):
    if chr(item) is not 'q' and chr(item) is not 'e':
        print("{}".format(chr(item)), end="")
