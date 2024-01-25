#!/bin/bash
# Bash script that sends a jason post request to a URL
# that has been passed as the first argument,
# and displays the body of the response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
