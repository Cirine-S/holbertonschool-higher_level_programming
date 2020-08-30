#!/bin/bash
# Bash script that displays the content_length of the body of the response
curl -sI "$1" | grep Content-Length | awk '{print $2}'
