#!/bin/bash
# This script sends a DELETE request to the URL passed as
# the first argument and displays the body of the response.
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Send a DELETE request and display the response body
response=$(curl -s -X DELETE "$url")

echo "Response Body:"
echo "$response"
