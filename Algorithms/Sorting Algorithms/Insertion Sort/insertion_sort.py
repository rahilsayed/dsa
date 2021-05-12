#Author: Rahil Sayed
#Date: 10/05/2021

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            #shifting all numbers greater than key to right
            arr[j + 1] = arr[j]
            j -= 1
        #j + 1 because j is one position less than the needed position because of the previous while loop condition
        arr[j + 1] = key
    return arr

arr = [1,0,2,9,3,8,4,7,5,6]
print(insertion_sort(arr))

#Time Complexity: O(n^2)
#Space Complexity: O(1)