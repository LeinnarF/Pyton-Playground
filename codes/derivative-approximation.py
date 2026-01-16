# Derivative Approximation using Finite Differences
'''
Algorithm:
1. Define the function f(x) for which the derivative needs to be approximated.
2. Choose a small value for h (step size).
3. Use the finite difference formula to approximate the derivative:   f'(x) ≈ (f(x + h) - f(x - h)) / (2 * h)
4. Implement the algorithm in Python.   
'''

def f(x):
    return x**2 + 3*x + 2
    # df/dx = 2x + 3

def derivative_approximation(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)

# Example usage
x_value = 2.0
approx_derivative = derivative_approximation(f, x_value)    
print(f"The approximate derivative of f(x) at x = {x_value} is {approx_derivative}")