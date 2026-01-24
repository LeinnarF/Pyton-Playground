# Permutation Group 
'''
A permutation group is a collection of bijective functions (permutations) from a set onto itself that is closed under the operation of composition and includes the identity permutation. Permutation groups are fundamental in the study of symmetry and group theory in mathematics.

Example:
Represent it in 2D array form:
1 2 3 4 5 6
4 2 5 3 1 6
This represents the permutation that maps:
1 -> 4 -> 3 -> 5 -> 1 

Not all permutations are cyclic, but all of them can be represented as a composition of cycles.
1 2 3 4 5 
2 1 5 3 4

This represents the permutation that maps:
1 -> 2 -> 1 and 3 -> 5 -> 4 -> 3

Implementation
Input: A list of mappings representing permutations of n elements. 
- The index of the list represents the original position, and the value at that index represents the mapped position.

Output: list of cycles representing the permutation.
'''

#              1  2  3  4  5  6
perm_group  = [4, 2, 5, 3, 6, 1]
perm_group2 = [2, 1, 5, 3, 4]
'''
Algorithm:
Input: a mapping reprsented as a list, where the index represents the original position.
Output: list of cycles representing the permutation.

Initialize: 
- list_of_cycles = []
- visited = [] 

'''

def is_mapped(perm, domain):
    for i in range(len(perm)):
        if i == domain-1:
            return perm[i]
        
def get_all_cycles(perm):
    visited = set()
    all_cycles = []
    
    for start in range(1, len(perm) + 1):
        if start in visited:
            continue
            
        current = start
        cycle = []
        
        while current not in visited:
            cycle.append(current)
            visited.add(current)
            current = perm[current - 1]
        
        if len(cycle) > 1 or cycle[0] != perm[cycle[0] - 1]:
            all_cycles.append(cycle)
    
    return all_cycles

print(get_all_cycles(perm_group2))