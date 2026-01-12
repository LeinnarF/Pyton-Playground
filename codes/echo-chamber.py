# Echo Chamber Effect Simulation
'''
The setup: 
Imagine three people connected in a line: Person A, Person B, and Person C.
- A is connected to B.
- B is connected to both A and C.
- C is connected to B.

Algorithm: In every round, each person shouts their current value to all their neighbors.

1. Everone simultaneously listens to their neighbors.
2. Your New Value is the sum of the value you neighbors shouted at you.
    If you have no messages, your value is 0.

Example:
A : 1
B : 0
C : 1

Round 1:
A hears from B (0) -> New A = 0
B hears from A (1) and C (1) -> New B = 2
C hears from B (0) -> New C = 0

Round 2:
A hears from B (2) -> New A = 2
B hears from A (0) and C (0) -> New B = 0
C hears from B (2) -> New C = 2

Round 3:
A hears from B (0) -> New A = 0
B hears from A (2) and C (2) -> New B = 4
C hears from B (0) -> New C = 0
'''

# Initial values for each person
person = {
    'A': 1,
    'B': 0,
    'C': 1
}

'''
Hint: If you treat the connections as a matrix A and the people as a vector v,
you are essentially calculating A * v.
This measures the number of walks or paths of length k in the graph.
'''

adjacency_matrix = [
    [0, 1, 0],  # Connections for A
    [1, 0, 1],  # Connections for B
    [0, 1, 0]   # Connections for C
]

vector_v = [person['A'], person['B'], person['C']]

def MatrixMultiplication(A, v):
    result = [0] * len(v)
    for i in range(len(A)):
        for j in range(len(v)):
            result[i] += A[i][j] * v[j]
    return result

rounds = 50
current_vector = vector_v

for round in range(rounds):
    current_vector = MatrixMultiplication(adjacency_matrix, current_vector)
    round += 1
    print(f'Round {round}', current_vector)