#Author: Rahil Sayed
#Date: 02/08/2021

'''
---------------------------------------------
Minimize the absolute difference
---------------------------------------------
Given three sorted arrays A, B and C of not necessarily same sizes.
Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
i.e. minimize | max(a,b,c) - min(a,b,c) |
---------------------------------------------
Example :
---------------------------------------------
Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:

1
Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.
---------------------------------------------
'''
#Note: We need minimum value of | max(a,b,c) - min(a,b,c) |. Hence, we can do this by maximizing min(a,b,c) OR minimizing max(a,b,c). We will maximize min(a,b,c) here by incrementing the pointer (since it is a sorted array).

def solve(A,B,C):
    i = j = k = 0
    min_diff = max(A[i],B[j],C[k]) + 1
    while i < len(A) and j < len(B) and k < len(C):
        #finding min and max of current group of elements
        minimum = min(A[i],B[j],C[k])
        maximum = max(A[i],B[j],C[k])

        diff = maximum - minimum

        #IMPORTANT(edge case): WHEN NEED MOD  | max(a,b,c) - min(a,b,c) |. Hence negative ans is invalid. Hence return the previous stored min_diff
        if diff < 0:
            return min_diff

        if diff < min_diff:
            min_diff = diff
        #incrementing the least min element, hence maximizing the minimum value.
        if A[i] == minimum:
            i += 1

        elif B[j] == minimum:
            j += 1
        
        elif C[k] == minimum:
            k += 1
    return min_diff

#Sample test case
print(solve( [ 1, 4, 5, 8, 10 ], [ 6, 9, 15 ],[ 2, 3, 6, 6 ]))

#Output: 
'''
1
'''

#Time Complexity: O(n)
#Space Complexity: O(1)


