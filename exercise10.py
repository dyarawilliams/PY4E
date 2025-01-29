# Date: December 15, 2024
# Exercise 10-1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

# Prompt the user for a file name
fname = input("Enter file name: ")
# If no file name is entered, use a default file
if len(fname ) < 1:
    fname = "mbox-short.txt"
# Open the specified file
fh = open(fname)
# Create an empty dictionary to store email addresses and their counts
counts = dict()

# Iterate through each line in the file
for line in fh:
    # Split the line into words
    words = line.split()
    # Checks if the line starts with "From" and has at least one word
    if len(words) > 0 and words[0] == "From":
         # Extract the email address from the second word
        email = words[1]
        # If the email is already in the dictionary, increment its count
        # Otherwise, add it to the dictionary with a count of 1
        counts[email] = counts.get(email, 0) + 1

# Create a list of tuples, where each tuple contains (count, email)
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

# Sort the list in descending order based on the count
lst.sort(reverse=True)

# Print the person who has the most commits
max_count, most_freq_sender = lst[0]
print(most_freq_sender, max_count)

# Exercise 10-2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# Create an empty dictionary to store hour counts
counts = dict()
# Iterate over each line in the file
for line in handle:
     # Split the line into words
    words = line.split()
     # Check if the line starts with "From" and has at least one word
    if len(words) > 0 and words[0] == "From":
        # Extract the full time from the 6th word
        full_time = words[5]
        # Extract the hour part from the full time
        hour = full_time.split(":")[0]
        
        # If the hour is not in the dictionary, add it with a count of 1
        if hour not in counts:
            counts[hour] = 1
        else:
            counts[hour] += 1
            
# Create a list of tuples, where each tuple contains (hour, count)
lst = list()
for key, val in list(counts.items()):
    lst.append((key, val))

# Sort the list of tuples by hour in ascending order
lst.sort()

# Print each hour and its corresponding count
for key, val in lst:
    print(key, val)


# Exercise 10-3: Write a program that reads a file and prints the letters in decreasing order of frequency.

# Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

# Prompt the user for a file name
fname = input("Enter file name: ")
# If no file name is entered, use a default file
if len(fname) < 1:
    fname = "mbox-short.txt"
# Open the specified file
fh = open(fname)
# Create an empty dictionary to store letter counts
counts = dict()

# Iterate through each line in the file
for line in fh:
    # Convert the line to lower case and only count the letters a-z. The program should not count spaces, digits, punctuation, or anything other than letters a-z
    line = line.lower()
    line = ''.join(e for e in line if e.isalpha())
    
    # Iterate through each character in the line
    for char in line:
        # If the character is not a letter, skip it
        if not char.isalpha():
            continue
        # If the character is not in the dictionary, add it with a count of 1
        if char not in counts:
            counts[char] = 1
        else:
            # Otherwise, increment its count
            counts[char] += 1

# Create a list of tuples, where each tuple contains (count, letter)
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

# Sort the list in descending order based on the count
lst.sort(reverse=True)

# Print the letters in decreasing order of frequency
for val, key in lst:
    print(key, val)