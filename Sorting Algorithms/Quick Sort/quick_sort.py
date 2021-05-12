#Author: Rahil Sayed
#Date: 12/05/2021

def partition(arr,start,end):
    #using the last element as pivot
    pivot = arr[end]
    #initialing i to -1
    i = start - 1
    #j iterates till the second last element i.e till before pivot
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    #increment i and then swap it with pivot i.e arr[end]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def quicksort(arr,start,end):
    if start < end:
        pivot_position = partition(arr,start,end)
        quicksort(arr,start,pivot_position - 1)
        quicksort(arr,pivot_position + 1,end)


a = [1,0,2,9,3,8,4,7,5,6]
quicksort(a,0,len(a) - 1)
print(a)


#Time Complexity: O(n*log(n))
#Space Complexity: O(log(n))