# Decimal to Hexadecimal Conversion

'''
Algorithm:
1. Start with the decimal number.
2. Divide the number by 16.
3. Record the remainder (0-15, where 10-15 are represented by A-F).
4. Update the number to be the quotient from the division.
5. Repeat steps 2-4 until the number is 0.
6. The hexadecimal representation is the remainders read in reverse order.
'''

starting_number = 654
current_number = starting_number
hexadecimal_representation = ""
hex_chars = "0123456789ABCDEF"
step_counter = 0

while current_number > 0:
    remainder = current_number % 16
    hexadecimal_representation = hex_chars[remainder] + hexadecimal_representation
    current_number = current_number // 16
    step_counter += 1
    print(f'Step {step_counter}: Current Number: {current_number}, Remainder: {remainder} ({hex_chars[remainder]}), Hex So Far: {hexadecimal_representation}')

print(f'Decimal: {starting_number}, Hexadecimal: {hexadecimal_representation}')
