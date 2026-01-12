'''
A jar contains 10 marbles 4 red and 6 blue. You randomly pick 2 marbles without replacement. What is the probability that at least one red marble is selected?

This problem is can be solve with hypergeometric distribution.
But for this exercise, we will solve it with Monte Carlo simulation.

'''

total_marbles = 10
red_marbles = 4
blue_marbles = 6
marbles = ['R'] * red_marbles + ['B'] * blue_marbles
selected_marbles = 2

successful_outcomes = 0
total_outcomes = 0
iterations = 100000

while total_outcomes < iterations:
    import random
    picked = random.sample(marbles, selected_marbles)
    if 'R' in picked:
        successful_outcomes += 1
    total_outcomes += 1

probability = successful_outcomes / total_outcomes
print(f'Estimated Probability of picking at least one red marble: {probability}')