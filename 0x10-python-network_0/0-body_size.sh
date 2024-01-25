#!/bin/bash
#  Script sends a request to a URL with curl,
# and displays the size of the body of the response
# the assumption here is that the url is provided as
# the first argument
curl -s "$1" | wc -c
