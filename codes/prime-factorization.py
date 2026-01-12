# Prime Factorization Implementation

def prime_factors(n):
    factors = []

    # Check for number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # n must be odd at this point, so we can skip even numbers
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors

number = 93
print(f'Prime factors of {number} are: {prime_factors(number)}')