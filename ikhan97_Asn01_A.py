'''
CS1026a 2023
Assingment 1 Project 1 - Part A
Isa Khan
251337547
ikhan97
09/21/2023
'''

print("Project One (1) - Part A : Fibonacci Sequence")

# Prompting for user input
sequence = int(input("Sequence ends at: ")) # Number sequence the program runs to


def fib_seq(base, increase, total_sequence, current_sequence):
    
    # Checking if that end of the sequence has been passed
    while current_sequence <= total_sequence:

        # Formatting and printing the current sequence
        formatted_number = f'{increase:,}'
        print(f"{current_sequence}: {increase} {formatted_number}")

        # Increasing the current values for the next piece of the sequence
        next_step = base + increase # Next step is the next number in the sequence
        base = increase # Base becomes the starting number for the next sequence
        increase = next_step # Increase becomes the next number in the sequence, after base
        current_sequence += 1

        # Calling method again while base case is not met
        return fib_seq(base, increase, total_sequence, current_sequence)
    return print("\nEND: Project One (01) – Part A\nIsa Khan ikhan97 251337547") 
    
# Printing starting cases    
if sequence >= 0:
    print("0: 0 0")
if sequence >= 1:
    print("1: 1 1")

# Calling recursive function
fib_seq(1,1,sequence,2)
