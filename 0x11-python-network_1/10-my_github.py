#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
  - first argument will be username
  - second argument will be password
"""
import sys
from requests.auth import HTTPBasicAuth
import requests


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    required_response = requests.get("https://api.github.com/user", auth=auth)
    print(required_response.json().get("id"))
