# Sum of primes up to 2,000,000

'''
Approach:
1. Use the Sieve of Eratosthenes algorithm to find all prime numbers up to 2,000,000.
2. Sum all the identified prime numbers.
'''


n = 2000000

def sieve_of_eratosthenes(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    p = 2

    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    
    prime_numbers = []
    for i in range(2, n + 1):
        if is_prime[i]:
            prime_numbers.append(i)
    return prime_numbers

prime_numbers = sieve_of_eratosthenes(n)
sum_of_primes = sum(prime_numbers)
print("Sum of all prime numbers up to", n, "is:", sum_of_primes)