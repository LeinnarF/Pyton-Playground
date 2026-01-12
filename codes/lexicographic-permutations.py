'''
The Problem:
What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Clarification:
A lexicographic permutation is an arrangement of digits in 
numerical order. For example, the lexicographic permutations
of the digits 0, 1 and 2 are:
012, 021, 102, 120, 201, 210

Digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (10  unique digits)
Order: 10! = 3,628,800 possible permutations
Index: We want the millionth permutation, which is at index 999,999

Rule:
Don't use library functions that generate permutations directly.

'''

# Start with small instance to verify logic

from sys import prefix


digits = "0123456789"





store_permutations = []

def permute(digits, prefix=""):
    if len(digits) == 0:
        store_permutations.append(prefix)
        return 
    for i in range(len(digits)):
        permute(digits[:i] + digits[i+1:], prefix + digits[i])


permute(digits)

# Find the 100th permutation (index 99)

position = 999999
result = store_permutations[position]
print(f"The millionth lexicographic permutation of {digits} is: {result}")