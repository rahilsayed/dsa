import random

def partition(arr,start,end):
    pivot = arr[start]
    i = start + 1
    for j in range(start + 1,end + 1):
        if arr[j] <= pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
    arr[i - 1],arr[start] = arr[start],arr[i - 1]
    pivot = i - 1
    return pivot


def randomPivot(arr,start,end):
    randpivot = random.randrange(start,end)
    arr[start],arr[randpivot] = arr[randpivot],arr[start]
    return partition(arr,start,end)


def quickSort(arr,start,end):
    if start < end:
        pi = randomPivot(arr,start,end)
        quickSort(arr,start,pi - 1)
        quickSort(arr,pi + 1,end)


arr = [1,0,2,9,3,8,4,7,5,6]
quickSort(arr,0,len(arr) - 1)
print(arr)
