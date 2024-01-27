#!/usr/bin/python3
"""
 a Python script that takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter.
Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - in the case where no letter is provided, will send `q=""`.
"""
import requests
import sys


if __name__ == "__main__":
    inputted_letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": inputted_letter}

    post_response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        given_response = post_response.json()
        if given_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(given_response.get("id"), given_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
