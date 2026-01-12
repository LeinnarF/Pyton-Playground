# The Sum o' Product is the Same

'''
Problem Statement:
Given a natural number a,b,c,d,e, it must statisfy the equation:
a + b + c + d + e = a * b * c * d * e

Write a program to find all such 5-digit combinations where the sum of the digits equals the product of the digits.

'''

solutions = []

def product_of_digits(digits):
    product = 1
    for digit in digits:
        product *= digit
    return product

for a in range(1, 10):  # a cannot be 0 for a 5-digit number
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(0, 10):
                    if a + b + c + d + e == a * b * c * d * e:
                        solutions.append((a, b, c, d, e))


# Print all found solutions
for solution in solutions:
    print(f"Solution found: {solution} -> Sum: {sum(solution)}, Product: {product_of_digits(solution)} ")


