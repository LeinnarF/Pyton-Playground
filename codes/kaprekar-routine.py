# Kaprekar's routine implementation in Python
# Given a four-digit number, perform Kaprekar's routine until reaching 6174
# algorithm:
# 1. Take any four-digit number that has at least two different digits.
# 2. Arrange the digits in descending and then in ascending order to get two four-digit numbers.
# 3. Subtract the smaller number from the larger number.
# 4. Repeat the process with the resulting number until you reach 6174.

starting_number = 1112
target_number = 6174
current_number = starting_number
iteration_count = 0

while current_number != target_number:
    # Convert the current number to a string to allow digit manipulation (Descending and Ascending)

    num_str = str(current_number).zfill(4) 
    descending_digits = ''.join(sorted(num_str, reverse=True))
    ascending_digits = ''.join(sorted(num_str))

    # Convert back to integers for subtraction
    larger_number = int(descending_digits)
    smaller_number = int(ascending_digits)

    current_number = larger_number - smaller_number
    iteration_count += 1

    print(f"Iteration {iteration_count}: {larger_number} - {smaller_number} = {current_number}")
