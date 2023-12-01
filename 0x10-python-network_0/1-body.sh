#!/bin/bash
# Display body only if reponse status is 200
view=$(curl -s -w %"{http_code}" -o response.txt -X GET http://"$1"); if [[ $view == "200" ]]; then cat response.txt; fi
