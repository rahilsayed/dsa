#Author: Rahil Sayed
#Date: 28/06/2021

'''
--------------------------------------------------
Noble Integer
--------------------------------------------------
Given an integer array, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.
If such an integer is found return 1 else return -1.
--------------------------------------------------
'''


def nobleInteger(A):
    arr = sorted(A)
    for i in range(len(arr)):
        if i < len(arr) - 1 and arr[i] == arr[i + 1]:   #skips the duplicates if any
            continue
        if len(arr[i + 1:])  == arr[i]:
            return 1
    return -1

#Sample test case
arr = [1,1,1]
print(nobleInteger(arr))

#Output:
'''
-1
'''

#Time Complexity: O(nlog(n))
#Space Complexity: O(1)

#Another Approach
'''
def nobleInteger(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                count += 1
        if count == arr[i]:
            return 1
    return -1
'''