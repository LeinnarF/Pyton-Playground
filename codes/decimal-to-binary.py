# Decimal to Binary Converter

'''
Algorithm:
1. Start with the decimal number.
2. Divide the number by 2.
3. Record the remainder (0 or 1).
4. Update the number to be the quotient from the division.
5. Repeat steps 2-4 until the number is 0.
6. The binary representation is the remainders read in reverse order.
'''

starting_number = 654
current_number = starting_number
binary_representation = ""

step_counter=0

while current_number > 0:
    remainder = current_number % 2
    binary_representation = str(remainder) + binary_representation
    current_number = current_number // 2
    step_counter += 1
    print(f'Step {step_counter}: Current Number: {current_number}, Remainder: {remainder}, Binary So Far: {binary_representation}')


print(f'Decimal: {starting_number}, Binary: {binary_representation}')

 