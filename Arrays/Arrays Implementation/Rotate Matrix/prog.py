#Author: Rahil Sayed
#Date: 29/06/2021

'''
--------------------------------------------------
Rotate Matrix
--------------------------------------------------
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
You need to do this in place.
--------------------------------------------------
Example:

If the array is:
[
    [1, 2],
    [3, 4]
]

Then the rotated array becomes:
[
    [3, 1],
    [4, 2]
]
--------------------------------------------------
'''


def rotate(a):
    n = len(a)
    #note: the middle element if any, never changes.
    #number of cycle or loops to rotate in the matrix
    for i in range(n // 2):
        #number of groups of elements in each cycle or loop i.e (-8,0,5,7) and (7,-7,-4,1) Hence, 2 groups.
        for j in range(i,n - i - 1):
            #i remains same in one cycle. j changes each cycle.
            #when moving through column, use j in row pos and i in col pos. 
            #when moving through row, use i in row pos and j in col pos.
            #when moving through both, use i in row pos and j in col pos.
            #top left with bottom left. bottom left with bottom right. bottom right with top right. top right with top left
            temp = a[i][j]                      #as row will change in next iterations
            a[i][j] = a[n-1-j][i]               #as column will change in next iterations
            a[n-1-j][i] = a[n-1-i][n-1-j]       #as row wil change in next iterations
            a[n-1-i][n-1-j] = a[j][n-1-i]       #as column will change in next iterations
            a[j][n-1-i] = temp
    return a

#Sample test case
a = [[-8,7,0],[1,-1,-7],[3,-4,-5]]
print(rotate(a))

#Output:
'''
[[3, 1, -8], [-4, -1, 7], [-5, -7, 0]]
'''

#Time Complexity: O(n^2)
#Space Complexity: O(1)