#!/bin/bash
# A script that sends a JSON POST request to a URL passed as the first
# argument, and displays the body of the response. Also send 
# a POST request with the contents of a file, passed with
# the filename as the second argument of the script, in the body of the request.
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

url=$1
json_file=$2

# Send a JSON POST request with the contents of the specified file and display the response body
response=$(curl -s -X POST -H "Content-Type: application/json" -d "@$json_file" "$url")

echo "Response Body:"
echo "$response"
