#!/usr/bin/python3
# 100-print_tebahpla.py

""""alternate between lower and uppercase while printing alphabet"""
i = 0
for num in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(num - i)), end="")
    i = 32 if i == 0 else 0
