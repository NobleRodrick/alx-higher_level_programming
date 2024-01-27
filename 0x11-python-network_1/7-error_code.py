#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
Usage: ./7-error_code.py <URL>
  - will handle HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    inputted_url = sys.argv[1]

    the_given_response = requests.get(inputted_url)
    if the_given_response.status_code >= 400:
        print("Error code: {}".format(the_given_response.status_code))
    else:
        print(the_given_response.text)
