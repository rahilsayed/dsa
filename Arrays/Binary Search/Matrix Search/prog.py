#Author: Rahil Sayed
#Date: 02/08/2021

'''
-----------------------------------------------------
Matrix Search
-----------------------------------------------------
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
-----------------------------------------------------
Example:
-----------------------------------------------------
Consider the following matrix:
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return 1 ( 1 corresponds to true )
-----------------------------------------------------
Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem
-----------------------------------------------------
'''

def searchMatrix(mat,key):
    row = 0
    col = len(mat[0]) - 1
    while row < len(mat) and col >= 0:
        if mat[row][col] == key:
            return 1
        elif mat[row][col] < key:
            row += 1
        elif mat[row][col] > key:
            col -= 1
    return 0

#Sample test case
mat = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

print(searchMatrix(mat,3))

#Output:
'''
1
'''

#Time Complexity: O(log(n))
#Space Complexity: O(1)
