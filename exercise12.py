# Date: January 5, 2025

# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page.

# You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.

import socket

url = input('Enter URL: ')
host = url.split('/')[2]

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()
except:
    print('URL is improperly formatted or non-existent.')
    quit()

# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

import socket

# Prompt user for URL
url = input('Enter URL: ')
# Extract host from URL
host = url.split('/')[2]

try:
    # Create socket and connect to host
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    # Send GET request
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    count = 0

    while True:
        # Receive data in chunks
        data = mysock.recv(512)
        if len(data) < 1:
            break
        count += len(data)
        # Display data up to 3000 characters
        if count <= 3000:
            print(data.decode(), end='')

    # Print total number of characters received
    print(f'\n\nTotal number of characters: {count}')

    # Close socket
    mysock.close()
except:
    # Handle improperly formatted or non-existent URL
    print('URL is improperly formatted or non-existent.')
    quit()

# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

import urllib.request

# Prompt user for URL
url = input('Enter URL: ')

try:
    # Open URL
    fhand = urllib.request.urlopen(url)

    count = 0

    for line in fhand:
        # Decode line and count characters
        count += len(line.decode())
        # Display data up to 3000 characters
        if count <= 3000:
            print(line.decode().strip())

    # Print total number of characters received
    print(f'\n\nTotal number of characters: {count}')
except:
    # Handle improperly formatted or non-existent URL
    print('URL is improperly formatted or non-existent.')
    quit()


# Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document and display the count of the paragraphs as the output of your program. Do not display the paragraph text, only count them. Test your program on several small web pages as well as some larger web pages.

import urllib.request
from bs4 import BeautifulSoup

# Prompt user for URL
url = input('Enter URL: ')

try:
    # Open URL
    fhand = urllib.request.urlopen(url)
    # Read HTML content
    html = fhand.read()
    # Parse HTML content
    soup = BeautifulSoup(html, 'html.parser')

    count = 0

    # Find all paragraph tags
    for tag in soup.find_all('p'):
        count += 1

    # Print total number of paragraphs
    print(f'Total number of paragraphs: {count}')
except:
    # Handle improperly formatted or non-existent URL
    print('URL is improperly formatted or non-existent.')
    quit()

# Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received. Remember that recv receives characters (newlines and all), not lines.

import socket

# Create socket and connect to host
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# Send HTTP GET request
cmd = f'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# Receive and process response
received_data = ''
while True:
    data = mysock.recv(4096).decode()
    if not data: 
        break
    received_data += data

# Find the position of the first blank line
pos = received_data.find('\r\n\r\n')
if pos == -1:
    pos = received_data.find('\n\n')    

# Display data after headers and blank line
if pos != -1:
    print(received_data[pos+4:])

mysock.close()