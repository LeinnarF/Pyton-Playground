# Collatz Conjecture (3n + 1 problem) 
# Algorithm: 
# 1. Start with any positive integer n.
# 2. If n is even, divide it by 2.
# 3. If n is odd, multiply it by 3 and add 1.
# 4. Repeat the process indefinitely.

starting_number = 216
target_number = 1
current_number = starting_number
iteration_count = 0
tracked_numbers = [current_number]

while current_number != target_number:
    if current_number % 2 == 0:
        current_number = int(current_number / 2)
    else:
        current_number = 3*(current_number)+1
    
    iteration_count += 1
    tracked_numbers.append(current_number)

    print(f'Iteration {iteration_count}: {current_number}')

print("Tracked numbers:", tracked_numbers)
highest_number = max(tracked_numbers)
print("Highest number reached:", highest_number, "at iteration", tracked_numbers.index(highest_number))