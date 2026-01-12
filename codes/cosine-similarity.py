# Cosine similarity implementation in Python

# Function to calculate cosine similarity between two vectors
# Algorithm:
# 1. Calculate the dot product of the two vectors.
# 2. Calculate the magnitude (norm) of each vector.
# 3. Divide the dot product by the product of the magnitudes to get the cosine

import math 

def dot_product(vec1, vec2):
    return sum(a * b for a, b in zip(vec1, vec2))

def magnitude(vec):
    return math.sqrt(sum(a ** 2 for a in vec))

def cosine_similarity(vec1, vec2):
    dot_prod = dot_product(vec1, vec2)
    mag1 = magnitude(vec1)
    mag2 = magnitude(vec2)
    
    if mag1 == 0 or mag2 == 0:
        raise ValueError("One or both vectors have zero magnitude.")
    
    return dot_prod / (mag1 * mag2)

vector_a = [1, 2, 3]
vector_2a = [2, 4, 6]

# Supposed vector_a is the basis, vector_2a is just a scaled version of vector_a
# Then, the cosine similarity should be 1, as they point in the same direction.
# But with different magnitudes.

similarity = cosine_similarity(vector_a, vector_2a)
print(f"Cosine Similarity: {similarity}")

# If cos = 1, the vectors are identical (same direction)
# If cos = 0, the vectors are orthogonal (90 degrees apart)
# if cost = -1, the vectors directions are opposite to each other

