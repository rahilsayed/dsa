#Author: Rahil Sayed
#Date: 02/08/2021

'''
-----------------------------------------------------
Search For a Range
-----------------------------------------------------
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
-----------------------------------------------------
Example:
-----------------------------------------------------
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
-----------------------------------------------------
'''


def getLeft(arr,key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key and arr[mid - 1] < key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def getRight(arr,key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key and (mid == len(arr) - 1 or arr[mid + 1] > key):
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def searchRange(arr,key):
    left = getLeft(arr,key)
    right = getRight(arr,key)
    return [left,right]

arr = [5,7,7,8,8,10]
print(searchRange(arr,8))
