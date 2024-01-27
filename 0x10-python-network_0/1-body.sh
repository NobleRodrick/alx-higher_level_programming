#!/bin/bash
# A script that takes in a URL, sends a GET request to the URL,
# and displays the body of the response.
f [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Send a GET request, get the response body, and display it for a 200 status code
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

if [ "$response" -eq 200 ]; then
    body=$(curl -s "$url")
    echo "Response Body:"
    echo "$body"
else
    echo "Unexpected HTTP status code: $response"
fi
