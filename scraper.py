import certifi
import urllib3
import urllib.request
from bs4 import BeautifulSoup
import re

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)

url = "URL_LINK_HERE"

#HTML of page
response = http.request('GET', url)
soup = BeautifulSoup(response.data, features="html.parser")

counter = 0

#Find all href tags with .pdf
#Take name, add to URL and retreive to set path
for link in soup.findAll(attrs={'href': re.compile(".pdf")}):
    getLinks = link.get('href')
    print(getLinks)
    url = "URL_LINK_HERE" + getLinks
    print(url)
    path = 'STORAGE_PATH_HERE'
    print(getLinks)
    path = path + getLinks
    urllib.request.urlretrieve(url, path)
    counter=counter+1
    print(counter)
