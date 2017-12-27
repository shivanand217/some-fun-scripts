import requests
import os
import sys
from time import sleep

from subprocess import call

# script helps to check whether a site is up or not
# by giving Command line argument like py script.py http://codeforces.com

if len(sys.argv) == 2:
    url = sys.argv[1]
    
    while(1):
        res = requests.get(url)
        if res.status_code == requests.codes.ok:
            s = "Site is Up"
            print(s)
            break
        else:
            print("Site is Down")
        sleep(5) # sleep for 5s
    
else:
    print("Enter Correct number of arguments")
