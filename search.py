# author: Shiv anand

import urllib
import json
from urllib.request import urlopen
from urllib.parse import urlencode

url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"
query = str(input("What do you want to search for ? "))

query = urlencode({'q': query})
response = urlopen(url + query).read()

data = json.loads(response)

results = data['responseData']['results']

for result in results:
    title = result['title']
    url = result['url']
    print(title + '; ' + url)
