#!/usr/bin/python3
"""
a Python script that takes 2 arguments in order to solve this challenge.
Listing the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    the_given_url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    the_given_response = requests.get(the_given_url)
    commits = the_given_response.json()
    try:
        for a in range(10):
            print("{}: {}".format(
                commits[a].get("sha"),
                commits[a].get("commit").get("author").get("name")))
    except IndexError:
        pass
