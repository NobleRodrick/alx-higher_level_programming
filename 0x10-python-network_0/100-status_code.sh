#!/bin/bash
# sends a request to a URL that has been passed as an argument,
# and displays only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
