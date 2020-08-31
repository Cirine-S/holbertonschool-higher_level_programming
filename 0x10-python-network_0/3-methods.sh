#!/bin/bash
# Bash script that displays the Allow field of the response body
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
