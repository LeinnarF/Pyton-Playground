'''
Problem:
If you take a stick and break it into three pieces
at random, what is the probability that the three pieces
can form a triangle?

approximate the probability that the three pieces can form a triangle

Triangle Inequality Theorem:
For any triangle with sides of lengths a, b, and c, 
the following conditions must be met:
    1. a + b > c
    2. a + c > b
    3. b + c > a

Imagine a stick of length 1 and break it at two random points,
x and y, 
These cuts three segments with lengths:
    x, y - x, and 1 - y (assuming x < y)

For these to form a triangle, the sume of any two segements
must be greater than the third segment. 

The longest segment must be less than 1/2 
because the other two must sum to more than 1/2 
to satisfy the triangle inequality.
    
'''
import random

length_of_stick = 1.0
num_trials = 1000000
successful_trials = 0

for _ in range(num_trials):
    x = random.uniform(0, length_of_stick)
    y = random.uniform(0, length_of_stick)

    # Ensure x is the smaller cut
    if x > y:
        x, y = y, x
    
    a = x
    b = y - x
    c = length_of_stick - y

    # Check the triangle inequality conditions
    if a + b > c and a + c > b and b + c > a:
        successful_trials += 1

probability = successful_trials / num_trials
print(f"Estimated Probability: {probability}")