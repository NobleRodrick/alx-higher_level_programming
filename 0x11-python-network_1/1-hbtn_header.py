#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the the_given_response
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as the_given_response:
        print(dict(the_given_response.headers).get("X-Request-Id"))
