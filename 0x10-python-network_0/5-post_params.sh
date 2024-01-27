#!/bin/bash
#A script that takes in a URL, sends a POST request to the passed URL,
# and displays the body of the response. A variable 'email' must be 
# sent with the value 'hr@holbertonschool.com'. A variable 'subject'
# must be sent with the value 'I will always be here for PLD'.
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request with the specified variables and display the response body
response=$(curl -s -X POST -d "email=$email&subject=$subject" "$url")

echo "Response Body:"
echo "$response"
