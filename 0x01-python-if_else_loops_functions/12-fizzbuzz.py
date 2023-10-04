#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
        """We are printing numbers and testing whether they are divisible
        by 3, 5 or both using fizz, buzz or fizzbuzz
        """
        for number in range(1, 101):
            if number % 3 == 0 and number % 5 == 0:
                print("FizzBuzz ", end="")
            elif number % 3 == 0:
                print("Fizz ", end="")
            elif number % 5 == 0:
                print("Buzz ", end="")
            else:
                print("{} ".format(number), end="")
