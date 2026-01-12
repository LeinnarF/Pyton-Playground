# Simple iteration example in Python
# Take the sum of numbers in a sequence and print the iteration count

sequence = {1,2,3,4,5,6,8,9,10}

sum = 0
for i in sequence:
    sum = sum + i
    itt = list(sequence).index(i) + 1
    print(f'Iteration {itt}: Sum: {sum}')
