#!/usr/bin/python3

def no_c(my_string):
    def_str = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            def_str += char
    return (def_str)
