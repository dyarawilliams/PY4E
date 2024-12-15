import re # impor the regex module for pattern matching

# Open the specified file for reading
# hand = open('regex_sum_42.txt')
hand = open('regex_sum_2106892.txt')

# Initialize a variable to store the final sum
final_total = 0

# Iterate through each line in the file
for line in hand:
    # Remove any trailing whitespace characters (like newlines) from the line
    line = line.rstrip()

    # Find all sequences of digits (numbers) in the line using regular expression
    x = re.findall('[0-9]+', line)

    # If there are any numbers found in the line
    if len(x) > 0:
        # Iterate through each found number
        for num in x:
            # Convert the number (which is a string) to an integer and add it to the final total
            final_total += int(num)
# Print the final calculated sum
print(final_total) # 343049