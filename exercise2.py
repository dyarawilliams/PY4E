# Exercise 2-2: 
# Write a program that uses input to prompt a user for their name and then welcomes them. Note that input will pop up a dialog box. Enter Sarah in the pop-up box when you are prompted so your output will match the desired output.
name = input("Enter your name: ")
print("Hello " + name)

# Enter your name: Chuck
# Hello Chuck
print("==============================")
# Exercise 2-3: 
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.

# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25

# We won’t worry about making sure our pay has exactly two digits after the decimal place for now. If you want, you can play with the built-in Python round function to properly round the resulting pay to two decimal places.

# You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.

hrs = input("Enter Hours: ")
rate_per_hrs = input("Enter rate per hours: ")
pay = float(hrs) * float(rate_per_hrs)
print("Pay: " + str(pay))

print("==============================")
# Exercise 2-4: 
# Assume that we execute the following assignment statements:

width = 17
height = 12.0
# For each of the following expressions, write the value of the expression and the type (of the value of the expression).

result1 = width//2
print(result1)
print(type(result1))
# The value of width//2 is 8, and the type is integer.

result2 = width/2.0
print(result2)
print(type(result2))
# The value of width/2.0 is 8.5, and the type is float.

result3 = height/3
print(result3)
print(type(result3))
# The value of height/3 is 4.0, and the type is float.

result4 = 1 + 2 * 5
print(result4)
print(type(result4))
# The value of 1 + 2 * 5 is 11, and the type is integer.

# Use the Python interpreter to check your answers.

print("==============================")

# Exercise 2-5:
# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
celsius = input("Enter a celsius temp: ")
c = float(celsius)
fahrenheit = c * (9/5) + 32
print(fahrenheit)