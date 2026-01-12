# Approximating the area of a circle using Monte Carlo method

import random

iterations = 1000000
inside_circle = 0

for _ in range(iterations):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y <= 1:
        inside_circle += 1
    
# Area of circle = (points inside circle / total points) * area of square
area_of_circle = (inside_circle / iterations) * 4
print(f"Approximated area of the circle: {area_of_circle}")


    