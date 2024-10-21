# Exercise 3-1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# 3.1: Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

# Declare and ask for input of hours and rate
hrs = input("Enter Hours:")
rate = input("Enter Rate:")

# Convert to float
h = float(hrs)
r = float(rate)

overtime = 0 

if h > 40:
    overtime = (h - 40) * (1.5 * r)
    pay = 40 * r + overtime
else:
    pay = h * r
print(pay)

# Exercise 3-2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input



# Exercise 3-3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

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

# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = input("Enter Score: ")

score = float(score) 

if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")