# Find the logest Collatz chain 

size = 1000000
init_num = [i for i in range(1, size)]

# Approach

# Store the length of each chain
chain_length = [0] * size

# Compute the length of the chain for each number
# Input: n in init_num Output: length of chain

def collatz_chain_length(n):
    length = 0
    current_number = n
    while current_number != 1:
        if current_number % 2 == 0:
            current_number = int(current_number / 2)
        else:
            current_number = 3 * (current_number) + 1

        length +=1 
    return length

# Itirate and append to chain_length
def compute_chain_lengths():
    for n in init_num:
        chain_length[n-1] = collatz_chain_length(n)
    
compute_chain_lengths()

# Find the maximum length and corresponding number
max_length = max(chain_length)
number_with_max_length = chain_length.index(max_length) + 1
print("Number with the longest Collatz chain:", number_with_max_length)
print("Length of the longest Collatz chain:", max_length)







