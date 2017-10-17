import requests
import re

#url = str(input('Enter a URL: '))

url = 'https://blog.anudeep2011.com/20-by-25/'

website = requests.get(url)

html = website.text

links = re.findall('"((html|ftp)s?://.*?)"', html)
emails = re.findall('([\w\.,]+@[\w\.,]+\.\w+)', html) # list 

print(len(emails))

print("\n Found {} links".format(len(links)))

for email in emails:
    print(email)
