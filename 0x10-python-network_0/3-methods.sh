#!/bin/bash
# Reguest availabe methods
curl -s -I -X OPTIONS http://"$1" | grep "Allow" | cut -d ":" -f2 | cut -d " " -f2-
