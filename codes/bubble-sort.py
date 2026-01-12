# Bubble Sort Algorithm

'''
Algorithm
1. initialize unsorted list
2. initialize index i and j
3. check if i < j
    if i < j => swap i and j
    else: check i < j+1
'''

unordered_list = [5,45,2,8,3,0,1,7,5,7]
steps = 0

def BubbleSort(arr):
    n = len(arr)
    global steps
    print(f'{steps} : {arr}')
    for i in range(n):
        isSwapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSwapped = True
        if not isSwapped:
            break
        steps += 1
        print(f'{steps} : {arr}')
    return arr

BubbleSort(unordered_list)