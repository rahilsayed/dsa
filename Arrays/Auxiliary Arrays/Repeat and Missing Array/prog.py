#Author: Rahil Sayed
#Date: 02/07/2021

'''
----------------------------------------
Repeat and Missing Number Array
----------------------------------------
You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Print A and B.
----------------------------------------
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
----------------------------------------
Note that in your output A should precede B.
----------------------------------------
Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4
----------------------------------------
'''

def sol(arr):
    n = len(arr)

    current_sum = sum(arr)
    correct_sum = sum(set(arr)) #We dont take correct sum with formula since b is still missing
    repeated_number = current_sum - correct_sum

    actual_sum = int(n * (n + 1) / 2)
    sum_without_repeated_number = sum(arr) - repeated_number
    missing_number = actual_sum - sum_without_repeated_number

    print(repeated_number, missing_number)

#Sample test case
arr = [1,4,5,3,3]
sol(arr)

#Output:
'''
3 2
'''

#Time Complexity: O(n)
#Space Complexity: O(1)