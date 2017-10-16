# Author: Shiv Anand
#This script scrapes the pdf and epub links that are there on any web page and downloads them.

import wget
import sys
import urllib
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser
from bs4 import BeautifulSoup

def process(url):

    page = urlopen(url)
    text = page.read()
    page.close()
    
    soup = BeautifulSoup(text)
    pdf = []
    epub = []
    
    for tag in soup.findAll('a', href=True):
        tag['href'] = urljoin(url, tag['href'])
        
        if 'pdf' in tag['href']:
            k = str(tag['href'])
            pdf.append(k)         
        elif 'epub' in tag['href']:
            k = str(tag['href'])
            epub.append(k)
    
    i=0
    j=0

    print('******** PDF on this URL ********')
    for k in pdf:
        print('Index(%d) <=> pdf = %s ' %(i , k))
        i += 1

    print()
    print('******** EPUB on this URL ********')
    for k in epub:
        print('Index(%d) <=> pdf = %s ' %(j , k))
        j += 1
        
    print('enter file type you want (pdf/epub): ', end=" ")
    fileType = str(input()) 
    
    print('Enter index number: ', end=" ")
    index_of_file_required = int(input())

    if fileType == 'pdf':
        print('file "'+ (pdf[index_of_file_required])+ '" is downloading....' )
        wget.download(pdf[index_of_file_required])
    else :
        print('file "'+ (epub[index_of_file_required])+ '" is downloading....' )
        wget.download(epub[index_of_file_required])

    print('Hurray... Download Completed ......... ')
    
# process('https://docs.djangoproject.com/en/1.11/')
# provide url from command line argument

def main():
    if len(sys.argv) <= 1:
        print('provide the url link')
        sys.exit(-1)
    else:
        url = sys.argv[1]
        process(url)
        
if __name__ == '__main__':
    main()
