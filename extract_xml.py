import urllib.request
import xml.etree.ElementTree as ET

# Prompt for the URL
url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
# Open the URL
uh = urllib.request.urlopen(url)
# Read the XML data from the URL using the urllib library
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
for result in counts:
    # Debug print the data :)
    # print(result.text)
    
    # Append the data to the list
    nums.append(int(result.text))

# Print the count and sum of the numbers

print('Count:', len(nums))
print('Sum:', sum(nums))