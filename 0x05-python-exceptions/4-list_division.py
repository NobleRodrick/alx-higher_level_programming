#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides the corresponding values of two lists"""
    brand_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            brand_list.append(div)
        return brand_list
