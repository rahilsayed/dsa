#Author: Rahil Sayed
#Date: 02/08/2021

'''
---------------------------------------------
Print intersection of 2 Sorted Arrays
---------------------------------------------
Intersection of 2 Sorted Arrays
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.
---------------------------------------------
Input Format
The first line contains T, the number of test cases. Following T lines contain:
Line 1 contains N1, followed by N1 integers of the first array
Line 2 contains N2, followed by N2 integers of the second array
Output Format
The intersection of the arrays in a single line
---------------------------------------------
Example
---------------------------------------------
Input:
1
3 10 17 57
6 2 7 10 15 57 246

Output:

10 57
---------------------------------------------
Input:
1
6 1 2 3 3 4 5 6
2 1 6

Output:
1 6
---------------------------------------------
'''

def intersectionElement(arr1,arr2,n1,n2):
    i = j = 0
    intersectionArr = []
    while i < n1 and j < n2:
        if arr1[i] > arr2[j]:
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            intersectionArr.append(arr1[i])
            i += 1
            j += 1
    return intersectionArr

T = int(input())
for t in range(T):
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    n1 = arr1[0]
    arr1 = arr1[1:]
    n2 = arr2[0]
    arr2 = arr2[1:]
    res = intersectionElement(arr1,arr2,n1,n2)
    print(*res)

#Sample Test Case:
'''
3
10 -9 -8 -7 -5 -4 -3 2 5 7 9
14 -8 -7 -6 -5 -3 -1 0 1 2 3 4 7 8 9
5 -8 -6 -2 4 9
3 -5 -4 -1
4 -1 0 4 6
9 -9 -8 -4 -3 -2 -1 1 2 5
'''

#Output:
'''
-8 -7 -5 -3 2 7 9

-1
'''

#Time Complexity: O(n)
#Space Complexity: O(n)