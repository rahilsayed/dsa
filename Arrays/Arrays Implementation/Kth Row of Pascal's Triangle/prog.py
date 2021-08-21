#Author: Rahil Sayed
#Date: 29/06/2021

'''
--------------------------------------------------
Kth Row of Pascal's Triangle
--------------------------------------------------
Given an index k, return the kth row of the Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
--------------------------------------------------
Example:
Input :
k = 3
Return :
[1,3,3,1]
--------------------------------------------------
Note: k is 0 based. k = 0, corresponds to the row [1].
Note: Could you optimize your algorithm to use only O(k) extra space?
k <= 100
--------------------------------------------------
'''

#Note: Any element in a pascal triangle is the sum of prev row: prev col and prev row: same col 
def getRow(k):
    
    pascal = [[0 for i in range(k + 1)] for j in range(k + 1)]
    for row in range(k + 1):    #k + 1 because we need the kth element
        pascal[row][0] = 1  #first element is always 1        
        for col in range(1, k + 1): 
            pascal[row][col] = pascal[row - 1][col] + pascal[row-1][col-1]
    return pascal[k]

#Sample test case
print(getRow(10))

#Output:
'''
[1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
'''

#Time Complexity: O(n^2)
#Space Complexity: O(n^2)

#Another approach : O(k) extra space
'''
def getRow(k):
    prev = [1]  #initialize with 1
    if k == 0:  #edge case: if k is 0 i.e first element
        return prev
    for row in range(1, k + 1): #Since first element is already defined, start iterating from 1
        curr = []
        for i in range(len(prev)):
            if i == 0:
                curr.append(1)  #first element is always 1
            else:
                curr.append(prev[i] + prev[i - 1])
        curr.append(1)  #Important: last element is always 1. Here according to logic we need to append 1
        prev = curr #set prev to curr
    return curr
'''