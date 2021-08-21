#Author: Rahil Sayed
#Date: 28/06/2021

'''
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:

Input:
1 2 3
4 5 6
7 8 9

Return:
[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]
'''

def diagonal(mat):
    n = len(mat)
    N = 2 * n - 1   #N gives the number of anti-diagonals in a matrix
    res_mat = [] * (N)
    for i in range(N):
        res_mat.append([])
    for i in range(n):
        for j in range(n):
            res_mat[i + j].append(mat[i][j])
    return res_mat

#Sample test case
arr = [[15,-8,-9],[-4,-7,17],[-17,3,14]]
print(diagonal(arr))

#Output:
'''
[[15], [-8, -4], [-9, -7, -17], [17, 3], [14]]
'''

#Time Complexity: O(N^2)
#Space Complexity: O(N)