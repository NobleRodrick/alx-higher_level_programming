#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header

"""
import sys
import requests


if __name__ == "__main__":
    inputted_url = sys.argv[1]

    the_url_request = requests.get(inputted_url)
    print(the_url_request.headers.get("X-Request-Id"))
