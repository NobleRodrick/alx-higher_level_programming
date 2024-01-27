#!/bin/bash
# A script that takes in a URL and displays
# all HTTP methods the server will accept.
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Send an OPTIONS request and display allowed HTTP methods
allowed_methods=$(curl -s -X OPTIONS -I "$url" | grep -i allow | awk '{print $2}')
echo "Allowed HTTP Methods: $allowed_methods"
