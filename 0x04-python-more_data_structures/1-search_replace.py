#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces occurences of an element with another in a new list"""
    replaced_list = list(map(lambda x: replace if x == search else x, my_list))
        return (replaced_list)
