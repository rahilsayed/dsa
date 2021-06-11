#Author: Rahil Sayed
#Date: 10/05/2021

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

arr = [1,0,2,9,3,8,4,7,5,6]
print(selection_sort(arr))

'''
Ouput:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

#Time Complexity: O(n^2)
#Space Complexity: O(1)