# Sieve of Eratosthenes implementation 

# Algorithm to find all prime numbers up to a specified integer n
'''
1. Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).
2. Start with the first number in the list (p=2), then cross all multiples of 2.
3. Next prime number is 3. Cross all multiples of 3.
4. Repeat the process for the next number in the list that is not crossed out.
'''

n = 100
# Initialize a boolean array "is_prime[0..n]" and set all entries as true.
is_prime = [True for _ in range(n+1)]
is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

p = 2

while (p * p <= n):
    # If is_prime[p] is not changed, then it is a prime
    if is_prime[p]:
        # Update all multiples of p
        for i in range(p * p, n + 1, p):
            is_prime[i] = False
    p += 1

# Collecting all prime numbers
prime_numbers = []
for i in range(2,n+1):
    if is_prime[i]:
        prime_numbers.append(i)

print("Prime numbers up to", n, "are:", prime_numbers)
