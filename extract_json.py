# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file

import urllib.request
import json

# Prompt for a URL
url = input('Enter location: ')
if len(url) < 1 : 
    # Use default URL if none is provided
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)

# Open the URL and read the data
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

# Parse the JSON data
info = json.loads(data)
print('Count:', len(info['comments']))

# Compute the sum of the comment counts
sum = 0
for item in info['comments']:
    sum += int(item['count'])
print('Sum:', sum)
