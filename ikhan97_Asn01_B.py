'''
CS1026a 2023
Assingment 1 Project 1 - Part B
Isa Khan
251337547
ikhan97
09/26/2023
'''

import math


print("Project One (1) - Part B : Prime Choice\n")

# Prompting for user input
start = int(input("Prime numbers starting with: ")) # Starting number of the range
end = int(input("and ending with: ")) # Ending number of the range

# Checking and flipping start and end numbers if required
if start > end:
    print(f"\nIncorrect input: {start} is greater than {end}"
          +"\nThe numbers have been automatically switched\n")
    placeholder = start # Placeholder is used to flip the values of start and end
    start = end
    end = placeholder

print(f"Prime numbers in the range from: {start} and {end} are:")

if start < 0:
    start = 0

# Looping through each number in the range given
for num in range (start, end+1):
    root = round(math.sqrt(num)) # Root is the square root of the number and is used to determine if it is prime
    prime = True

    # Checking if number is prime
    for value in range (2, root+1):
        if num % value == 0:
            prime = False
    if num == 0 or num == 1:
        prime = False    
    # Printing prime numbers
    if prime:
        print(f"{num} is prime")

print("\nEnd Part One (01) - Project B\nIsa Khan ikhan97 251337547")