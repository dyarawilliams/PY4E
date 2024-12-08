# Exercise 9-1: Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

fhand = open("words.txt")
d = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in d:
            d[word] = 1
        else: 
            d[word] += 1
print(d) 
# Output :
# {'Writing': 1, 'programs': 2, 'or': 1, 'programming': 1, 'is': 2, 'a': 3, 'very': 2, 'creative': 1, 'and': 5, 'rewarding': 1, 'activity': 1, 'You': 1, 'can': 4, 'write': 1, 'for': 1, 'many': 2, 'reasons': 1, 'ranging': 2, 'from': 2, 'making': 1, 'your': 2, 'living': 1, 'to': 16, 'solving': 1, 'difficult': 1, 'data': 1, 'analysis': 1, 'problem': 2, 'having': 1, 'fun': 1, 'helping': 1, 'someone': 1, 'else': 1, 'solve': 1, 'This': 1, 'book': 1, 'assumes': 1, 'that': 4, '{\\em': 1, 'everyone}': 1, 'needs': 1, 'know': 2, 'how': 2, 'program': 1, 'once': 1, 'you': 4, 'program,': 1, 'will': 1, 'figure': 1, 'out': 1, 'what': 2, 'want': 1, 'do': 5, 'with': 2, 'newfound': 1, 'skills': 1, 'We': 2, 'are': 3, 'surrounded': 1, 'in': 2, 'our': 5, 'daily': 1, 'lives': 1, 'computers': 5, 'laptops': 1, 'cell': 1, 'phones': 1, 'think': 1, 'of': 5, 'these': 1, 'as': 1, 'personal': 1, 'assistants': 1, 'who': 1, 'take': 1, 'care': 1, 'things': 3, 'on': 2, 'behalf': 2, 'The': 1, 'hardware': 1, 'current-day': 1, 'essentially': 1, 'built': 1, 'continuously': 1, 'ask': 1, 'us': 2, 'the': 6, 'question': 1, 'What': 1, 'would': 2, 'like': 2, 'me': 1, 'next': 2, 'Our': 1, 'fast': 1, 'have': 1, 'vasts': 1, 'amounts': 1, 'memory': 1, 'could': 2, 'be': 1, 'helpful': 1, 'if': 1, 'we': 5, 'only': 1, 'knew': 2, 'language': 2, 'speak': 1, 'explain': 1, 'computer': 2, 'it': 1, 'If': 1, 'this': 1, 'tell': 1, 'tasks': 1, 'were': 1, 'reptitive': 1, 'Interestingly,': 1, 'kinds': 2, 'best': 1, 'often': 1, 'humans': 1, 'find': 1, 'boring': 1, 'mind-numbing': 1}

# Exercise 9-2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

# Sample Line:

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Sample Execution:

# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

fname = input("Enter file name: ")
if len(fname ) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
counts = dict()
for line in fh:
    words = line.split()
    if len(words) > 0 and words[0] == "From":
        # if words[2] not in counts:
        #     # counts[words[2]] = 1
        # else:
        #     counts[words[2]] += 1
        counts[words[2]] = counts.get(words[2], 0) + 1
print(counts)


# Exercise 9-3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

fname = input("Enter file name: ")
if len(fname ) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
counts = dict()
for line in fh:
    words = line.split()
    if len(words) > 0 and words[0] == "From":
        counts[words[1]] = counts.get(words[1], 0) + 1
print(counts)

# Exercise 9-4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

fname = input("Enter file name: ")
if len(fname ) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
counts = dict()
max_key = ''
for line in fh:
    words = line.split()
    if len(words) > 0 and words[0] == "From":
        counts[words[1]] = counts.get(words[1], 0) + 1
for key in counts:
    if counts[key] > counts.get(max_key, 0):
        max_key = key
        
print(max_key, counts[max_key])


# Exercise 9-5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

fname = input("Enter file name: ")
if len(fname ) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
d = dict()
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) > 0 and words[0] == "From":
        email = words[1]
        words2 = email.split('@')
        domain = words2[1]
        d[domain] = d.get(domain, 0) + 1
print(d)