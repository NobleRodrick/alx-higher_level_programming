#!/bin/bash
# Bash script takes in a url, sends a get request to the url
# and displays the body of the response(200 status code)
curl -sL "$1"
