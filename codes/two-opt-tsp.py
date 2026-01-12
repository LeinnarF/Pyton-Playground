# Solving TSP using 2-opt heuristic
'''
Algorithm steps:
1. Start with an initial tour (e.g., the order of cities as given).
2. Calculate the total distance of the current tour.
3. Iterate through all possible pairs of edges in the tour.
4. For each pair of edges, perform a 2-opt swap by reversing the order of the cities between the two edges.
5. Calculate the total distance of the new tour after the swap.
6. If the new tour is shorter, update the current tour to the new tour.


'''

distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def tour_cost(tour, distance_matrix):
    cost = 0
    num_cities = len(tour)
    for i in range(num_cities):
        cost += distance_matrix[tour[i]][tour[(i + 1) % num_cities]]
    return cost

# Test
# Best tour is 3 -> 1 -> 0 -> 2 with cost 80
# print(tour_cost([3, 1, 0, 2], distance_matrix))  

def swap_2opt(tour, i, k):
    """
    Perform a 2-opt swap operation on a tour.
    
    The 2-opt algorithm is a local search heuristic used in the Traveling Salesman Problem (TSP).
    This function reverses a segment of the tour between indices i and k (inclusive),
    which can potentially improve the tour by reducing crossing edges.
    
    Args:
        tour (list): A list representing the current tour, where each element is a city/node.
        i (int): The starting index of the segment to reverse (inclusive).
        k (int): The ending index of the segment to reverse (inclusive).
    
    Returns:
        list: A new tour with the segment between indices i and k reversed.
    
    Example:
        >>> tour = [0, 1, 2, 3, 4, 5]
        >>> swap_2opt(tour, 2, 4)
        [0, 1, 4, 3, 2, 5]
    """
    new_tour = tour[:i] + tour[i:k+1][::-1] + tour[k+1:]
    return new_tour

def two_opt(distance_matrix):
    num_cities = len(distance_matrix)
    current_tour = list(range(num_cities))
    improved = True

    while improved:
        improved = False
        current_cost = tour_cost(current_tour, distance_matrix)

        for i in range(1, num_cities - 1):
            for k in range(i + 1, num_cities):
                new_tour = swap_2opt(current_tour, i, k)
                new_cost = tour_cost(new_tour, distance_matrix)

                if new_cost < current_cost:
                    current_tour = new_tour
                    current_cost = new_cost
                    improved = True

    return current_tour, current_cost

best_tour, best_cost = two_opt(distance_matrix)
print(f'Best tour: {best_tour} with cost: {best_cost}')

