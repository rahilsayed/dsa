#Author: Rahil Sayed
#Date: 06/07/2021

'''
--------------------------------------------------
Flip
--------------------------------------------------
You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, Sn. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters S[L], S[L+1], …, S[R]. By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised. If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.
--------------------------------------------------
Notes:
--------------------------------------------------
Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
--------------------------------------------------
For example: 
    S = 010

    Pair of [L, R] | Final string
    _______________|_____________
    [1 1]          | 110
    [1 2]          | 100
    [1 3]          | 101
    [2 2]          | 000
    [2 3]          | 001

    We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. 

    So, we return [1, 1].
--------------------------------------------------
Another example:

    If S = 111
    No operation can give us more than three 1s in final string. 
    So, we return empty array [].
==================================================

'''

#This problem can be solved by Kandane's Algorithm.
#In this approach, we replace '0' by 1 and '1' by 1.
#That is because 0 when flipped will give 1 and we want maximum number of 1. Hence, maximum number of zeroes.
#Using Kandane's algorithm on this new updated array, we get a range with maximum count of zeroes.


def flip(A):
    n = len(A)
    #Replace '0' in array by 1 and '1' by -1
    arr = []
    for i in range(n):
        if A[i] == '0':
            arr.append(1)
        else:
            arr.append(-1)
    #Creating two pointer l,r to keep track of range.
    #Create temp pointer ptr to traverse.
    #curr_summ for sum so far
    #max_sum for maximum sum.
    curr_sum = 0
    max_sum = 0
    ptr = 0
    l = 0
    r = 0
    for i in range(n):
        #Adding values i.e 1 and -1
        #1 will increase the value. i.e number of 0
        #-1 will decrease the value. i.e number of 1
        curr_sum += arr[i]
        #if new sum is greater than max_sum, then update max_sum and keep the current range in l,r pointers.
        if curr_sum > max_sum:
            max_sum = curr_sum
            l = ptr
            r = i
        #if sum becomes negative, then number of 1 are greater. Hence, the array subarray till now 
        #will not be the correct ans anyways. Hence discarding the current subarray by updating the ptr pointer.
        #Also change curr_sum to 0 as we are starting again.
        elif curr_sum < 0:
            curr_sum = 0
            ptr = i + 1
    #Important: As given in question, if no flipping is required, then return []
    #Hence check if max_sum is zero.
    if max_sum == 0:
        return []
    #As it is 1 based indexing in question, return values with one added.
    return [l + 1,r + 1]

#Sample Test Case:
arr = ['1','0','0','1','0','0']
print(flip(arr))

#Output:
'''
[2,6]
'''
#Time Complexity: O(n)
#Space Complexity: O(1)


#Another approach:
#Similar to previous approach, the only change is, instead of taking sum,
#we are taking the count of 0 and 1 in array.
#If 0 then increase count by 1, and if 1 then decrease count by 1.
'''
def flip(A):
    n = len(A)
    count = 0
    max_count = 0
    l = r = 0
    ptr = 0
    for i in range(n):
        if A[i] == '0':
            count += 1
        else:
            count -= 1
        if count > max_count:
            max_count = count
            l = ptr 
            r = i 
        elif count < 0:
            ptr = i + 1
            count = 0
    if max_count == 0:
        return []
    return [l+1,r+1]
'''





    

    