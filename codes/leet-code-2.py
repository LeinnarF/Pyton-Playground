# Add Two numbers
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Plan of Attack:
1. Given two list, both lists are in reverse order.
2. Reverse both lists to get the actual numbers.
3. Store each element in a string, then convert to integer.
4. Add both integers.
5. Convert the sum back to string, then to a list of integers.
'''


def reverse_list(lst):
    return lst[::-1]

def to_integer(lst):
    num_str = ''.join(map(str, lst))
    return int(num_str)

def to_list(num):
    list_num = []
    for digit in str(num):
        list_num.append(int(digit))
    return list_num

def add_two_numbers(l1, l2):
    rev_l1 = reverse_list(l1)
    rev_l2 = reverse_list(l2)
    
    num1 = to_integer(rev_l1)
    num2 = to_integer(rev_l2)
    
    total = num1 + num2
    
    result_list = to_list(total)
    
    return reverse_list(result_list)

l1 = [5,7,8]
l2 = [9,4,7,3]

result = add_two_numbers(l1, l2)
print(result)