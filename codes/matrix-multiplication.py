# Matrix Multiplication

'''
Applying linear trasformation in a matrix

Algorithm:
1. Define two matrices A and B.
2. Initialize a result matrix C with appropriate dimensions.
3. Loop through rows of A.
4. Loop through columns of B.

'''

import numpy as np

matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_B = [
    [1,0],
    [0,1],
    [1,1]
]

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(elem) for elem in row))
    print()

def matrix_multiply(A, B):
    
    # The resultant matrix C will have dimensions len(A) x len(B[0])
    rows= len(A)
    cols= len(B[0])
    
    resultant_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            for k in range(len(B[0])):
                resultant_matrix[i][j] += A[i][k] * B[k][j]
    return resultant_matrix



result = matrix_multiply(matrix_A, matrix_B)
print("Resultant Matrix after Multiplication:")
print_matrix(result)





