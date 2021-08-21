#Author: Rahil Sayed
#Date: 02/08/2021

'''
-----------------------------------------------------
Rotated Sorted Array Search
-----------------------------------------------------
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).
You are given a target value to search. If found in the array, return its index, otherwise return -1.
You may assume no duplicate exists in the array.
-----------------------------------------------------
Input : [4 5 6 7 0 1 2] and target = 4
Output : 0
-----------------------------------------------------
Note : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
-----------------------------------------------------
'''

def search(arr,key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] <= arr[high]:
            if key > arr[mid] and key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if key >= arr[low] and key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1

#Sample Test Case
arr = [4,5,6,7,0,1,2]
print(search(arr,1))

#Output:
'''
5
'''

#Time Complexiy: O(log(n))
#Space Complexity: O(1) 