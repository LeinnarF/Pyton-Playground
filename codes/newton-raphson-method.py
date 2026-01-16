# Finding the root of a function using the Newton-Raphson method

'''
Algorithm:
1. Define the function f(x) for which the root needs to be found.
2. Define the derivative f'(x) of the function.
3. Choose an initial guess x0 for the root.
4. Set a tolerance level for convergence (e.g., tol = 1e-7).
5. Iterate using the formula: x_{n+1} = x_n - f(x_n) / f'(x_n)
6. Stop when the absolute difference between successive approximations is less than the tolerance level.
'''

def f(x):
    return x**2 + 3*x + 2

def derivative_approximation(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)

N = 100
i = 0
tol = 1e-7
init_x = -1.0
current_x = init_x

while i < N: 
    f_current = f(current_x)
    df_current = derivative_approximation(f, current_x)

    # watcher
    print(f"Iteration {i}: x = {current_x}, f(x) = {f_current}, f'(x) = {df_current}")

    if df_current == 0:
        print("Derivative is zero. No solution found.")
        break

    next_x = current_x - f_current / df_current

    if abs(next_x - current_x) < tol:
        print(f"Root found: {next_x} after {i+1} iterations")
        break

    current_x = next_x
    i += 1

    if i == N:
        print("Maximum iterations reached. No solution found.")

print(f"Approximate root after {i} iterations is {current_x}")