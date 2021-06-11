#Author: Rahil Sayed
#Date: 11/05/2021

def merge(arr1,arr2):

    arr3 = [None] * (len(arr1) + len(arr2))   
    i = j = k = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
            k += 1
        else:
            arr3[k] = arr2[j]
            j += 1
            k += 1
    
    #add the remaining extra values from arr1 or arr2 directly in arr3
    while i < len(arr1):
        arr3[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        arr3[k] = arr2[j]
        j += 1
        k += 1 

    return arr3


def merge_sort(a):

    #base case
    if len(a) == 1:
        return a

    b1 = []
    for i in range(len(a)//2):
        b1.append(a[i])

    b2 = []
    for i in range(len(a)//2, len(a)):
        b2.append(a[i])

    #recursive case
    b1 = merge_sort(b1)
    b2 = merge_sort(b2)

    #it always passes sorted lists to merge as it starts by passing one element
    c = merge(b1,b2)
    return c


#sample test case
arr = [1,0,2,9,3,8,4,7,5,6]
print(merge_sort(arr))

'''
Ouput:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

#Time Complexity: O(n*log(n))
#Space Complexity: O(n)