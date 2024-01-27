#!/bin/bash
# This is a csript that takes in a URL as an argument,
# sends a GET request to the URL, and displays the body of the response. 
# Also, a header variable X-School-User-Id must be sent with the value 98.
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1
user_id_header="X-School-User-Id: 98"

# Send a GET request with the specified header and display the response body
response=$(curl -s -H "$user_id_header" "$url")

echo "Response Body:"
echo "$response"
