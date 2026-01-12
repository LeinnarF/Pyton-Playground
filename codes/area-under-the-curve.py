# Monte Carlo method to approximate the area under the cuvve
# I = exp(-sin(xy) -x^y) sqrt(1 + x^3 y^3) from x= 0 to 1 and y=0 to 1

import random
import math

def f(x, y):
    return math.exp(-math.sin(x * y) - x**y) * math.sqrt(1 + x**3 * y**3)

iterations = [100, 1000, 10000, 100000, 1000000]
area_sum = 0


for iteration in iterations:
    for _ in range(iteration):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        area_sum += f(x, y)


    area_under_curve = area_sum / iteration
    print(f"Approximated area under the curve with {iteration} iterations: {area_under_curve:.6f}")