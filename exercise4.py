# Date: October 27, 2024
# Exercise 4-1: 
# Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.
import random

for i in range(10):
    x = random.random()
    print(x)

print("=================================")
# Exercise 4-2: 
# Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.

# repeat_lyrics()

# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')


# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()

# The error message I recieved was a Name Error that says 'repeat_lyrics' is not defined.

# Exercise 4-3: 
# Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics. What happens when you run this program?

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

repeat_lyrics()
# When I run the program it defines 'repeat_lyrics' and 'print_lyrics' and last prints the lyrics because it calls 'print_lyrics' within the called function, so functions are not executed until the function is called.
 
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.

print("=================================")

# Exercise 4-4: 
# What is the purpose of the “def” keyword in Python?
# a) It is slang that means “the following code is really cool”
# b) (answer) It indicates the start of a function
# c) It indicates that the following indented section of code is to be stored for later
# d) b and c are both true
# e) None of the above

# Exercise 4-5: 
# What will the following Python program print out?

def fred():
   print("Zap")

def jane():
   print("ABC")

jane()
fred()
jane()

# a) Zap ABC jane fred jane
# b) Zap ABC Zap
# c) ABC Zap jane
# d) (correct) ABC Zap ABC
# e) Zap Zap Zap

print("=================================")

# Exercise 4-6: 
# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# 4.6: Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.

def computepay(h, r):
    try:
        h = float(h)
        r = float(r)
        overtime = 0 

        if h > 40:
            overtime = (h - 40) * (1.5 * r)
            pay = 40 * r + overtime
        else:
            pay = h * r
        return pay
    except Exception as e:
        print("Please enter a number")

hrs = input("Enter Hours: ")
pay = input("Enter pay: ")
p = computepay(hrs, pay)
print("Pay: ", p)

print("=================================")

# Exercise 4-7: 
# Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

#  Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly to test the various different values for input.

def computegrade(score):
    try:
        score = float(score) 
        if score >= 0.9 and score <= 1.0:
            print("A")
        elif score >= 0.8 and score <= 1.0:
            print("B")
        elif score >= 0.7 and score <= 1.0:
            print("C")
        elif score >= 0.6 and score <= 1.0:
            print("D")
        elif score < 0.6 :
            print("F")
        else:
            print("Bad Score")
    except Exception as e:
        print("Bad score")

score = input("Enter Score: ")
computegrade(score)