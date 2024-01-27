#!/bin/bash
# A script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response.
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Send a request, get the response body, and display its size in bytes
size=$(curl -s "$url" | wc -c)
echo "Size of the response body: $size bytes"
