# Date: November 3, 2024

# Exercise 5.1
# Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the integers. If the user enters anything other than a integers, detect their mistake using try and except and print an error message and skip to the next integers.

# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

count = 0
total = 0
average = None

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try :
        num = float(num)
        total = total + num
        count = count + 1
        average = total / count
    except:
        print('Invailed Input')
        continue
    
print (total, count , average)

# Exercise 5.2
# Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     try:
#         num = int(num)
#         if largest is None or num > largest: 
#             largest = num
#         if smallest is None or num < smallest: 
#             smallest = num
#     except:
#         print('Invalid input')

# print("Maximum is", largest)
# print("Minimum is", smallest)

# Output 
# Enter a number: 7
# Enter a number: 2
# Enter a number: bob
# Invalid input
# Enter a number: 10
# Enter a number: 4
# Enter a number: done
# Maximum is 10
# Minimum is 2