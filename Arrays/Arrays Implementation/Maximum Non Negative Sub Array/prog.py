#Author: Rahil Sayed
#Date: 25/06/2021

'''
--------------------------------------------
Find out the maximum sub-array of non negative numbers from an array.

The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).
--------------------------------------------
Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]
--------------------------------------------
Note 1: If there is a tie, then compare with segment’s length and return segment which has maximum length

Note 2: If there is still a tie, then return the segment with minimum starting index
--------------------------------------------
'''

def check(curr, max_so_far):
    if sum(curr) > sum(max_so_far):
        max_so_far = curr
    elif sum(curr) == sum(max_so_far):
        if len(curr) > len(max_so_far):
            max_so_far = curr
        elif len(curr) == len(max_so_far):
            if max_so_far and (curr[0] > max_so_far[0]):
                max_so_far = curr
    return max_so_far

def maxset(arr):
    curr = []
    max_so_far = []
    for i in arr:
        if i >= 0:
            curr.append(i)
        else:
            max_so_far = check(curr,max_so_far)
            curr = []
    max_so_far = check(curr,max_so_far)
    return max_so_far

#sample test case
arr = [1, 2, 5, -7, 2, 3]
print(maxset(arr))

#output:
'''
[1, 2, 5]
'''

#Time Complexity: O(n)
#Space Complexity: O(n^2)

