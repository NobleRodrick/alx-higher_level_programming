#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me
# and ends up getting the message "You got me!".
# Send a request to 0.0.0.0:5000/catch_me and capture the response in a variable
response=$(curl -s -X PUT --data "user_id=42" 0.0.0.0:5000/catch_me)

# The server response containing "You got me!" will be displayed without using echo, cat, etc.
response
