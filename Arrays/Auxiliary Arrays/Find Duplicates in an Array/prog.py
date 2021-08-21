#Author: Rahil Sayed
#Date: 02/07/2021

'''
--------------------------------------------------
Find Duplicate in Array
--------------------------------------------------
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.
--------------------------------------------------
Sample Input:
[3, 4, 1, 4, 1]

Sample Output:
1
--------------------------------------------------
Note: If there are multiple possible answers ( like in the sample case above ), output any one.

Note: If there is no duplicate, output -1
--------------------------------------------------
'''


def repeatedNumber(arr):
    n = max(arr)    #since 1 to n integers, max i arr will be the last number or max + 1 will be the size
    actual_sum = (n * (n + 1)//2)   #formula
    current_sum = sum(arr)
    repeated_number = current_sum - actual_sum
    if repeated_number == 0:
        return -1
    return repeated_number

#Sample test case
arr = [10 ,9 ,7 ,6 ,5 ,1 ,2 ,3 ,8 ,4 ,7]
print(repeatedNumber(arr))

#Output:
'''
7
'''

#Time Complexity: O(n)
#Space Complexity: O(1)