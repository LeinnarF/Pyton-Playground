'''
Heron's Method (Square Root Approximation)

Find the square root of a number S
where S > 0 using Heron's Method.
let x be your initial guess, ie., the closest perfect square to S.

Algorithm:
1. Take your initial guess x.
2. Divide S your gues (S / x).
3. Take the average of the that result and you current guess
    X = (x + (S / x)) / 2
4. Repeat with the new guess
'''

# Number to find the square root of

square_root_of = 6540 

# Initial guess for the square root, ie., sqrt(16) = 4
initial_guess = 1

current_guess = initial_guess

def formula(S, x):
    return (x + (S / x)) / 2

iteration = 0
tolerance = 0.00001 # Acceptable error margin

# Note: Not perfect squares are irrational numbers

while True:
    new_guess = formula(square_root_of, current_guess)
    iteration += 1
    print(f"Iteration {iteration}: Current Guess = {new_guess}")
    if abs(new_guess - current_guess) < tolerance:
        break
    current_guess = new_guess

print(f"Approximate square root of {square_root_of} is {new_guess} after {iteration} iterations.")
