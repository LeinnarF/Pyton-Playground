'''
The Secretary Problem

The Secretary Problem is a famous problem in optimal stopping theory. The problem can be described as follows:

You are interviewing candidates for a secretary position. The candidates are interviewed one by one in random order. After each interview, you must decide whether to hire that candidate or continue interviewing the next candidate. Once you reject a candidate, you cannot go back and hire them later. The goal is to maximize the probability of hiring the best candidate.

Algorithm:
1. Let n be the total number of candidates.
2. Calculate the threshold k = n / e (where e is the base of the natural logarithm, approximately equal to 2.71828).
3. Interview and reject the first k candidates, keeping track of the best candidate among them.
4. From the (k+1)-th candidate onward, hire the first candidate who is better than the best candidate from the first k candidates

Implement with Monte Carlo Simulation to estimate the probability of successfully hiring the best candidate.

'''
import random
import math

n = 100
iterations = 10000
success_count = 0
k = int(n / math.e)

for _ in range(iterations):
    candidates = list(range(n))
    random.shuffle(candidates)

    best_so_far = max(candidates[:k])
    hired = False

    for candidate in candidates[k:]:
        if candidate > best_so_far:
            if candidate == n - 1:
                success_count += 1
            hired = True
            break

    if not hired and candidates[-1] == n - 1:
        success_count += 1

probability = success_count / iterations
print(f"Estimated probability of hiring the best candidate: {probability:.4f}")

