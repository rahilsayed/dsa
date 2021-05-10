#Author: Rahil Sayed
#Date: 05/10/2021

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1],arr[j]
    return arr

#sample test case
arr = [1,9,2,8,3,7,4,6,5,0]
print(bubble_sort(arr))

#Time Complexity: O(n^2)
#Space Complexity: O(1)
