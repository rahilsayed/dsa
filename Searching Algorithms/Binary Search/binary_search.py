#Author: RahIL Sayed
#Date: 05/10/2021

def binary_search(arr,key):
    start = 0
    end = len(arr) - 1
    while end >= start:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        elif arr[mid] > key:
            end = mid - 1

#sample test case        
arr= [10,12,15,19,25,30]
print(binary_search(arr,10))

#Time Complexity: O(log(n))
#Space Complexity: O(1)