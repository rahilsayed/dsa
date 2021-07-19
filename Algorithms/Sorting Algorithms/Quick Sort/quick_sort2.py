#Author: Rahil Sayed
#Date: 28/06/2021

def quickSort(arr,start,end):
    i = start
    j = end - 1
    pivot = end
    #while i <= j:
    while arr[i] < arr[pivot]:
        i += 1
    #first condition in while is to check whether j is greater than start. We dont need to check for i as we are already doing it in outermost while
    while j >= start and arr[j] >= arr[pivot]:
        j -= 1
    #this condition stops the elements from swapping in case where j become less than i as outermost while is not checked yet
    if i <= j:
        arr[i],arr[j] = arr[j],arr[i]


    arr[i],arr[pivot] = arr[pivot],arr[i]
    #check whether the partition exist or not
    if start < i - 1:
        quickSort(arr,start,i - 1)
    if i + 1 < end:
        quickSort(arr,i + 1,pivot)

#Sample test case
arr = [1,0,2,9,3,8,4,7,5,6]
quickSort(arr,0,len(arr) - 1)
print(arr)