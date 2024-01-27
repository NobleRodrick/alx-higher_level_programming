#!/usr/bin/python3
"""A Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
Usage: ./2-post_email.py <URL> <email>
  - will display the body of the response.
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    the_url = sys.argv[1]
    email_value = {"email": sys.argv[2]}
    encoded_data = urllib.parse.urlencode(email_value).encode("ascii")

    request = urllib.request.Request(the_url, encoded_data)
    with urllib.request.urlopen(request) as the_given_response:
        print(the_given_response.read().decode("utf-8"))
