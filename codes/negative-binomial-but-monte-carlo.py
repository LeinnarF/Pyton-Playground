'''
Solves a negative binomial problem using Monte Carlo simulation.

A basketball player has 70% free throw success rate. What is the probability that she makes her 5th successful free throw on their 7th attempt? 

If solved with negative binomial distribution.
x = 7 (number of trials)
k = 5 (number of successful trials)
p = 0.7 (probability of success on each trial)
q = 0.3 (probability of failure on each trial) 

'''

total_attempts = 7
successful_shots = 5
success_rate = 0.7
failure_rate = 1 - success_rate
import random

successful_outcomes = 0
total_outcomes = 0
iterations = [100, 1000, 10000, 100000, 1000000]

for iteration in iterations:
    while total_outcomes < iteration:
        shots = []
        for attempt in range(total_attempts):
            if random.random() < success_rate:
                shots.append(1)  # Successful shot
            else:
                shots.append(0)  # Missed shot
        if sum(shots) == successful_shots and shots[-1] == 1:
            successful_outcomes += 1
        total_outcomes += 1
    probability = successful_outcomes / total_outcomes
    print(f"Estimated probability after {iteration} iterations: {probability}")