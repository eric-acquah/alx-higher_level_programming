#!/usr/bin/bash
# Send http request to server
curl -sI http://"$1" | grep "Content-Length" | cut -d " " -f2
