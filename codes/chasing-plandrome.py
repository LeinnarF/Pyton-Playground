# Palindrome Checker
# Algorithm
# 1. Take your current number and reverse it.
# 2. Add the reversed number to the current number.
# 3. Check if the result is a palindrome.
# if it is palidrome, stop.
# if it is not, repeat steps 1-3 with the new number.

# Checking for palindromes starting from numbers 1 to 99

init_list = [i for i in range(1, 501)]
current_number = init_list[0]
isPalindrome = False
iteration = 0

def PalindromeForNumber(number):
    current = number
    iteration = 0

    while iteration < 1000:
        if str(current) == str(current)[::-1]:
            print(f"Number: {number}, Palindrome: {current}")
            return
        current += int(str(current)[::-1])
        iteration += 1
    print(f"Number: {number} has no palindrome")

for i in init_list:
    PalindromeForNumber(i)


# while isPalindrome == False:
#     iteration +=1 
#     if str(current_number) == str(current_number)[::-1]:
#         isPalindrome = True
#         print(f"Palindrome {current_number} found after {iteration} iterations")
#     else:
#         reversed_number = int(str(current_number)[::-1])
#         current_number = current_number + reversed_number
#         print(f"Iteration {iteration}: Current number is {current_number}")
#     if iteration > 1000:
#         print(f"No palindrome found after {iteration} iterations, stopping.")
#         break
