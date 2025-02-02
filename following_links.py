import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Enter url, count and position
url = input('Enter - ')
count = int(input('Enter count: '))
pos = int(input("Enter position: ")) - 1

# Retrieve the html
for _ in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    # Update the url
    url = tags[pos].get('href', None)
    
    print("Retrieving: ", url)

