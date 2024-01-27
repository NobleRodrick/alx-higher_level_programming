#!/bin/bash
# script code that sends a request to a URL passed as an argument,
# and displays only the status code of the response.
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Send a request and extract the status code using curl
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")

# Display the status code
echo "Status Code: $status_code"
