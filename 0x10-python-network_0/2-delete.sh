#!/bin/bash
# script that sends a DELETE request to a
# URL with curl and displays the body of the response
curl -sX DELETE "$1"
