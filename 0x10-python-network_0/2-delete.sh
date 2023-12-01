#!/bin/bash
# Send a delete request to server
curl -s -X DELETE http://"$1" -o >(cat)
