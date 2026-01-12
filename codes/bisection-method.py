# Finding the root of a function using the Bisection Method

'''
Algorithm:
1. Define the function f(x) for which we want to find the root.
2. Choose two initial points a and b such that f(a) and f(b) have different signs.
3. Calculate the midpoint c = (a + b) / 2.
4. Check the value of f(c):
    - If f(c) is close enough to 0 (within a specified tolerance), then
        c is the root.
    - If f(c) has the same sign as f(a), then set a = c.
    - If f(c) has the same sign as f(b), then set b = c.
5. Repeat steps 3 and 4 until the root is found within the desired tolerance or
   the maximum number of iterations is reached.

'''


# def midpoint(a, b):
#     return (a + b) / 2

# # interval [a, b]
# a = 1 
# b = 5 
# tolerance = 1e-5
# max_iterations = 10000
# counter = 0

# if f(a) * f(b) >= 0:
#     print("The function must have different signs at the endpoints a and b.")
#     print(f"f(a={a}) =", f(a), f"f(b={b}) =", f(b))
#     exit()
# while counter < max_iterations:
#     c = midpoint(a, b)
#     if abs(f(c)) < tolerance:
#         print(f"Root found: {c} after {counter} iterations")
#         break
#     if f(c) * f(a) < 0:
#         b = c
#     else:
#         a = c
#     counter += 1
# Pack it as a function

def bisection_method(func, a, b, tolerance=1e-5, N =10000):
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have different signs at the endpoints a and b.")
    
    i = 0
    while i < N:
        c = (a + b) / 2
        if abs(func(c)) < tolerance:
            return c, i
        if func(c) > 0:
            b = c
        else:
            a = c
        i += 1
    raise ValueError("Maximum number of iterations reached without finding root.")

# Example
def f(x):
    return 5*x**5 + x + 1

# interval
a = -1
b = 1
root, iterations = bisection_method(f, a, b)
print(f"Root found: {root} after {iterations} iterations")