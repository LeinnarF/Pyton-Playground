# Look-and-say sequence generator

'''
Algorithm:
To get the next number, read the digits of the previous number aloud, counting how many digits appear in a row.

Suppose we start with "1":
1. Start with "1".
    Read it as "one 1" -> Next number is "11".

2. Take "11".
    Read it as "two 1s" -> Next number is "21".

3. Take "21".
    Read it as "one 2, then one 1" -> Next number is "1211".

4. Take "1211".
    Read it as "one 1, one 2, then two 1s" -> Next number is "111221". 
'''

starting_number = "1"

def look_and_say(sequence, n):
    result = [sequence]
    for _ in range(n -1):
        current = result[-1]
        next_sequence = ""
        count = 1
        for i in range(1, len(current)):
            if current[i] == current[i - 1]:
                count += 1
            else:
                next_sequence += str(count) + current[i - 1]
                count = 1
        next_sequence += str(count) + current[-1]
        result.append(next_sequence)
    return result

n = 10
sequences = look_and_say(starting_number, n)
for index, seq in enumerate(sequences):
    print(f"Term {index + 1}: {seq}")
