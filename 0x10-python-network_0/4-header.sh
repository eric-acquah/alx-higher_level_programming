#!/bin/bash
# Add custom header to GET request
curl -s -H "X-School-User-Id: 98" -X GET http://$1
