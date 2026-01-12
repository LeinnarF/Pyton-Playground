# Solving Traveling Salesman Problem using brute-force approach

import itertools

distance_matrix = [
    [0, 9, 2, 3, 5],
    [9, 0, 4, 1, 7],
    [2, 4, 0, 4, 8],
    [3, 1, 4, 0, 10],
    [5, 7, 8, 10, 0]
]

num_cities = len(distance_matrix)
cities = list(range(num_cities))

for row in range(len(distance_matrix)):
    print(distance_matrix[row])

print(f'Cities: {cities}')

min_cost = float('inf')

for perm in itertools.permutations(cities):
    print(f'Current permutation: {perm}')
    current_cost = 0
    for i in range(num_cities):
        current_cost += distance_matrix[perm[i]][perm[(i + 1) % num_cities]]
    print(f'Cost for this permutation: {current_cost}')
    if current_cost < min_cost:
        min_cost = current_cost

print(f'Minimum cost of traveling through all cities: {min_cost}')
