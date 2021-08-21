#Author: Rahil Sayed
#Date: 05/07/2021

'''
--------------------------------------------------
Maximum Absolute Difference
--------------------------------------------------
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
--------------------------------------------------
For example,

A=[1, 3, -1]
 
f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5
 
So, we return 5.
--------------------------------------------------
'''

'''
-------------------------------------------
Self Explaination:

|A[i] - A[j]| + |i - j|

 A[i] - A[j] + i - j
 A[i] - A[j] - i + j
-A[i] + A[j] + i - j
-A[i] + A[j] - i + j

Create two arrays to store: B for A[i] + i
                            C for A[i] - i

To get maximum results from these equations, first value must be max ans second must be min.
Hence,
 (A[i] + i) - (A[j] + j) = max(B) - min(B)
 (A[i] - i) - (A[j] - j) = max(C) - min(C)
-(A[i] - i) + (A[j] - j) = max(C) - min(C)
-(A[i] + i) + (A[j] + j) = max(B) - min(B)


Therefore, ans would be max(max(B) - min(B),max(C) - min(C))
-------------------------------------------
'''

def maxAbsDiff(A):
    B = [A[i] + 1 for i in range(len(A))]
    C = [A[i] - i for i in range(len(A))]
    return max(max(B) - min(B),max(C) - min(C))

#Sample test case
arr = [-344 ,654 ,629 ,-514 ,6 ,-368 ,-50 ,817 ,155 ,-729 ]
print(maxAbsDiff(arr))

#Output:
'''
1548
'''
#Time complexity: O(n)
#Space Complexity: O(n)