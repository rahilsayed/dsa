#Author: Rahil Sayed
#Date: 05/07/2021

'''
--------------------------------------------------
Max Distance
--------------------------------------------------
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].
If there is no solution possible, return -1.
--------------------------------------------------
Example :

A : [3 5 4 2]
Output :
 2 
for the pair (3, 4)
--------------------------------------------------
'''



def maximumGap(arr):
    n = len(arr)

    #We need to find maximum of j - i, such that A[i] <= A[j] 
    #Hence, for maximum, we need max of j and min of i
    #i.e Rmax since j is used for max from right
    #and Lmin since i i used for min from left

    #Create an auxillary array Lmin to store minimum element from left according to index
    Lmin = [0] * n
    Lmin[0] = arr[0]
    for i in range(1,n):
        Lmin[i] = min(arr[i],Lmin[i - 1])

    #Create an auxillary array Rmax to store maximum element from right according to index.
    #Note: We start storing from right so that we get an array with proper grouping w.r.t to Lmin element.
    Rmax = [0] * n
    Rmax[-1] = arr[-1]
    for i in range(n - 2,-1,-1):
        Rmax[i] = max(arr[i],Rmax[i + 1])

    print('Lmin: ',Lmin)
    print('Rmax: ',Rmax)

    #Important: Initialize max_diff to -1 so that differences <= 0 are ignored
    max_diff = -1
    i = j = 0
    while i < len(arr) and j < len(arr):
        #Given condition
        if Lmin[i] <= Rmax[j]:
            #if current group is greater than the previous max_diff, update max_diff
            max_diff = max(max_diff,j - i)
            #Increment j only because i is already minimum and condition is satisfied
            j += 1
        else:
            #As condition isnt satisfied, increment i and check again
            i += 1
    return max_diff

#Sample Test Case
arr = [9 ,8 ,7 ,-9 ,-1]
print(maximumGap(arr))

#Output:
'''
1
'''
#Time Complexity: O(N)
#Space Complexity: O(N)

'''
#Another Approach:
#Time Complexity: O(N^2)
#Space Complexity: O(1)

for i in range(len(arr)):
    for j in range(i + 1,len(arr)):
        if arr[i] <= arr[j]:
            max_diff = max(max_diff,j - i)
return max_diff
'''