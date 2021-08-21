#Author: Rahil Sayed
#Date: 02/07/2021

'''
--------------------------------------------------
First Missing Integer
--------------------------------------------------
Given an unsorted integer array, find the first missing positive integer.
--------------------------------------------------
Example:

1. Given [1,2,0] return 3

2. Given [3, 4, -1, 1] return 2

3. Given [-8, -7, -6] return 1
--------------------------------------------------
Your algorithm should run in O(n) time and use constant space.
--------------------------------------------------
'''

#Note: 0 is an integer as it is a whole number.
# All whole numbers right of 0 are positive integers, while on the left are negative integers.

#Approach 1:
#This approach intends to put each element in array in its respective index position i.e (i - 1) 
#At the end, the index of the first number not at its correct index, i.e (i + 1) will give us the answer.

#For more information: https://www.youtube.com/watch?v=-lfHWWMmXXM
def firstMissingPositive(arr):
    n = len(arr)
    for i in range(n):
        #arr[i] - 1 beacuse 0 based indexing
        correct_pos = arr[i] - 1
        #Important:The answer will always be in the range of the length of arr i.e between 1 and n + 1(if its last number).
        while arr[i] >= 1 and arr[i] <= n and arr[i] != arr[correct_pos]:
            #if element at i is not at the correct position, then swap it with the correct one.
            arr[i],arr[correct_pos] = arr[correct_pos],arr[i]
            #Important: the value of correct position will change due swap.
            #Hence, we need to again assign it the correct value.
            correct_pos = arr[i] - 1
    
    #check whether the index i.e i + 1(due to 0 based indexing) is equal to the element at that position.
    #if not then return i + 1
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
    
    #Important: If no number is missing, that is all element are from 1 to n, then n + 1 becomes the first missing element
    return (n + 1)

#Approach 2: 
'''
def firstMissingPositive(arr):
    n = len(arr)
    check = 0

    # Check if 1 is present in array or not
    for i in range(n):
        if arr[i] == 1:
            check = 1
            break

    # If 1 is not present
    if check == 0:
        return(1)

    # Changing values to 1
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = 1

    # Updating indices according to values
    for i in range(n):
        #Imporant: Kind of a formula. Try to remember.
        #Updating the element at index value equal to the current index value by adding the value of n to them.
        # % n is used to make sure the index are in range of length of the array. arr[i] - 1 is used due to 0 based indexing.
        arr[(arr[i] - 1) % n] += n

    # Finding which index has value less than n
    for i in range(n):
        if arr[i] <= n:
            return(i + 1)

    # If array has values from 1 to n
    return(n + 1)
'''

#Approach 3: (ONLY FOR POSITIVE INTEGERS)
#The APPROACH 2 is for both positive and negative, while this is only for positive integers.
#This approach intends to select the positive integer element at index equal to the element at current index position,
#then multiply it by -1.
#Hence, after that operation, the index at which the element is positive will be the first missing integer.
'''
def firstMissingPositive(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] <= n - 1 and arr[i] >= 1:
            arr[arr[i] - 1] *= -1
            
    for i in range(n):
        if arr[i] >= 0:
            return (i + 1)
            
            
    return (n + 1)
'''

#Sample test case
arr = [3, 4, -1, 1]
print(firstMissingPositive(arr))

#Output:
'''
2
'''

#Time Complexity: O(n)
#Space Complexity: O(1)

