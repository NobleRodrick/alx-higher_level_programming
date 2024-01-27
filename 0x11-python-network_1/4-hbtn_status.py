#!/usr/bin/python3
"""
python script that Fetches https://alx-intranet.hbtn.io/status.
"""
import requests


if __name__ == "__main__":
    defined_response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(defined_response.text)))
    print("\t- content: {}".format(defined_response.text))
