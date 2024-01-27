#!/usr/bin/python3
"""
 Script that Fetches https://alx-intranet.hbtn.io/status.
 using the urllib module
"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as the_given_response:
        body = the_given_response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
