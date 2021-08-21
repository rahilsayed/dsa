#Author: Rahil Sayed
#Date: 28/06/2021

'''
--------------------------------------------------
Largest Number
--------------------------------------------------
Given a list of non negative integers, arrange them such that they form the largest number.
--------------------------------------------------
For example:
Given [3, 30, 34, 5, 9], the largest formed number is 9534330
--------------------------------------------------
Note: The result may be very large, so you need to return a string instead of an integer.
--------------------------------------------------
'''
#Note: This problem can be solved by a simple bubble sort approach, forming two combinations and comparing in each iteration
def largestNumber(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            comb1 = str(arr[j]) + str(arr[j + 1])
            comb2 = str(arr[j + 1]) + str(arr[j])
            if comb2 > comb1:
                arr[j],arr[j + 1] = arr[j + 1],arr[j]

    ans = ''
    for i in arr:
        ans += str(i)
    return ans

#Sample test case
arr = [15,31,26,16,44]
print(largestNumber(arr))

#Output:
'''
4431261615
'''

#Time Complexity: O(N^2)
#Space Complexity: O(1)

 