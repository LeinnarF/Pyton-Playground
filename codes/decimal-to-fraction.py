# decimal to fraction 

number = 0.125 

# to fraction
numerator = number.as_integer_ratio()[0]
denominator = number.as_integer_ratio()[1]

fraction = {f'{numerator}/{denominator}'}

print(f'Number: {number}, Fraction: {fraction}')
