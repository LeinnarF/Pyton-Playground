# How long does it take for a number to reach a single digit
'''
Algorithm:
1. Start with a given positive integer.
2. Multiply all the digits of the number to get a new number.
3. Repeat the process with new number
4. Stop when the number is a single digit.
'''
import random

starting_number = random.randint(10, 2000)
print(f"Starting number: {starting_number}")
current_number = starting_number
iteration = 0

num_str = str(current_number)

# Repeat until we reach a single digit
while len(num_str)>1:

    # Multiply all the digits together
    product = 1
    for digit in num_str:
        product *= int(digit)
    current_number = product
    num_str = str(current_number)
    iteration += 1
    print(f"Iteration {iteration}: {current_number}")

print(f"It took {iteration} iterations for {starting_number} to reach a single digit.")