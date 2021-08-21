#Author: Rahil Sayed
#Date: 28/06/2021

'''
--------------------------------------------------
Add One To Number
--------------------------------------------------
You are given a non-negative number represented as an array of digits.
Example: 123 is represented as [1,2,3]
You must add 1 to the number ( increment the number represented by the digits ) and return the required array or list.
The digits are stored such that the most significant digit is at the head of the list.
--------------------------------------------------
Example:

If the vector has [1, 2, 3], the returned vector should be [1, 2, 4],
as 123 + 1 = 124
--------------------------------------------------
Note: 
Your returned array must not have any leading zeros. Example:
Input:
[0,0,2,1]

Ouput:
[2,2] // no leading zeros
--------------------------------------------------
Maximum size of the array is 300 so avoid converting it to a string or an integer. Instead, try to think of what happens when 1 is added to the number.
--------------------------------------------------
'''

def plusOne(A):
    # write your method here
    carry = 1
    i = len(A) - 1
    while carry == 1 and i >= 0:
        if A[i] < 9:
            A[i] += carry
            carry = 0
        else:
            A[i] = 0    #Edge case: if the element is 9, change to 0 and carry 1 forward
            i -= 1
    if i < 0 and carry == 1:    #Edge case: if all element are zero, then append 1 in the starting
        A.insert(0, 1)
    while(A[0] == 0):
        A = A[1:]   #Remove trailing zeros by slicing
    return A


#Sample test case
print(plusOne([9,9,9,9,9,8,9]))

#Output:
'''
[9, 9, 9, 9, 9, 9, 0]
'''

#Time Complexity: O(N)
#SPace Complexity: O(1)

'''
Alternate Approach:
def plusOne(arr):
    arr = A
    start = 0
    end = len(arr) - 1
    while arr[end] == 9 and end >= start:
        arr[end] = 0
        end -= 1
    if end < start and arr[end] == 0:
        arr.insert(0,1)
    else:
        arr[end] += 1
    while arr[0] == 0:
        arr = arr[1:]            
    return arr
'''
