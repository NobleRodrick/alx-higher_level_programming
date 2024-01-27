#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
Usage: ./3-error_code.py <URL>
  - Will handle the hyper text transfer protocol errors.
"""
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as the_given_response:
            print(the_given_response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
