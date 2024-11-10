# Date: November 3, 2024

fruit = 'banana'

# Exercise 6.1
# Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

index = 4
while index >= 0:
    letter = fruit[index]
    print(letter)
    index = index - 1

# Exercise 6.2
# Given that fruit is a string, what does fruit[:] mean?
# The operator [n:m] returns the part of the string from the “n-th” character to the “m-th” character, including the first but excluding the last.

# Exercise 6.3
# Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

# Exercise 6.4
# There is a string method called count that is similar to the function in the previous exercise. Read the documentation of this method at:

# https://docs.python.org/library/stdtypes.html#string-methods

# Write an invocation that counts the number of times the letter a occurs in “banana”.
'banana'.count('a')

# Exercise 6.5
# Slicing strings

# Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence: 0.8475'

# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

colon_pos = str.find(":")
print(float(str[colon_pos + 1:].strip()))

# Exercise 6.6
# String methods

# Read the documentation of the string methods at

# https://docs.python.org/library/stdtypes.html#string-methods.

# You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.

# The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.