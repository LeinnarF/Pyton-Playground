# Sophie Germain Primes

'''
The goal is to see how long a prime number can keep its prime status under specific transformations.

Algiorithm:
1. Start with a prime number p.
2. Calculate the next potential number (N) use the formula:
    N = 2p + 1
3. Check if N is prime.
    If N is prime, repeat step 2 with N as the new p.
    If N is not prime (composite), stop the process.
'''

starting_prime = 3
current_prime = starting_prime
iteration = 0

# is Prime?
def isPrime(n):
    # If n is zero or one
    if n <= 1:
        return False
    # Check from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def SophieGermainPrimes(prime):
    return 2 * prime + 1

while isPrime(current_prime):
    print(f"Iteration {iteration}: {current_prime} is prime.")
    current_prime = SophieGermainPrimes(current_prime)
    iteration += 1

print(f"Iteration {iteration}: {current_prime} is not prime. Stopping the process.")
