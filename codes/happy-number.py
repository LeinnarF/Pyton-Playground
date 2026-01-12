# Happy Number Checker
# algorithm to determine if a number is a happy number
# 1. take a positive integer n
# 2. square each of its digits separately
# 3. add those squares together to get a new number
# 4. repeat steps 2 and 3 until the number equals 1 (happy) 
# if it loops endlessly in a cycle that does not include 1 (not happy)

starting_number = 20
current_number = starting_number
target_number = 1
iteration_count = 0


def numSquareSum(n):
    total = 0
    for digit in str(n):
        total += int(digit) ** 2
    return total

while current_number != target_number:
    current_number = numSquareSum(current_number)
    iteration_count += 1
    print(f"Iteration {iteration_count}: Sum of squares = {current_number}")

    if current_number == target_number:
        print(f"{starting_number} is a happy number!")
        break
    elif iteration_count > 100:  # Arbitrary limit to prevent infinite loops
        print(f"{starting_number} is not a happy number.")
        break
