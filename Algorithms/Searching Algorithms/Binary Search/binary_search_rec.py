#Author: Rahil Sayed
#Date: 10/05/2021

def binary_search_rec(arr,key,start,end):
    #base condition
    if start > end:
        return 

    mid = (start + end) // 2  #in case of large values, we use mid = (start + (end - start)) // 2

    #base condition
    if arr[mid] == key:
        return mid

    #recursive condition
    if arr[mid] > key:
        return binary_search_rec(arr,key,start,mid - 1)
    elif arr[mid] < key:
        return binary_search_rec(arr,key,mid + 1,end)

#sample test case
arr = [1,3,6,10,16,22]
print(binary_search_rec(arr,10,0,len(arr) - 1))

'''
Output:
3
'''


#Time Complexity: O(log(n))
#Space Complexity: O(1)