#!/bin/bash
# Send a post request with some data
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" http://"$1"
