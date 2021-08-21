#Author: Rahil Sayed
#Date: 26/07/2021

'''
--------------------------------------------------
Maximum Sum Contiguous SubArray
--------------------------------------------------
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
--------------------------------------------------
Example:
--------------------------------------------------
Given the array [-2,1,-3,4,-1,2,1,-5,4], the contiguous subarray [4,-1,2,1] has the largest sum = 6.
--------------------------------------------------
For this problem, return the maximum sum.
--------------------------------------------------
'''


#Kadane's algorithm is used in this problem.
#The simple idea of Kadane’s algorithm is to look for all positive contiguous segments of the array (sum_so_far is used for this). And keep track of maximum sum contiguous segment among all positive segments (max_sum is used for this). Each time we get a positive-sum compare it with max_sum and update max_sum if it is greater than max_sum. Note: l,r pointers are only used if we also want range of indexes.

def maxSubArray(arr):
    sum_so_far = 0
    max_sum = min(arr)
    l = 0
    r = 0
    ptr = 0
    for i in range(len(arr)):
        sum_so_far += arr[i]
        if max_sum < sum_so_far:
            max_sum = sum_so_far
            l = ptr
            r = i
        #if the sum_so_far is < 0 i.e a negative number, it is not going to contritbute in increasing the value ahead
        #Hence, we do not need the sum_so_far and we start again from the next element.
        if sum_so_far < 0:
            sum_so_far = 0
            ptr = i + 1

            
    #print('l: ',l)
    #print('r: ',r)
    return max_sum
#sample test case
arr = [-68 ,78 ,95 ,59 ,77 ,-89 ,-100 ,-48 ,68 ,28]
print(maxSubArray(arr))
#Output:
'''
309
'''
#Time Complexity: O(N)
#Space Complexity: O(1)

#Another approach using consecutive sums array.
# Time complexity: O(N^2)
# Space Complexity: O(N) 
'''
def maxSubArray(arr):
    #generating consecutive sum array
    x_arr = [0] * len(arr)
    x_arr[0] = arr[0]
    for i in range(1,len(arr)):
        x_arr[i] = x_arr[i - 1] + arr[i]

    max_sum = min(x_arr)
    max_l = -1
    max_r = -1
    for l in range(len(arr)):
        for r in range(l + 1,len(arr)):
            if l - 1 < 0:
                curr_sum = x_arr[r]
            else:
                curr_sum = x_arr[r] - x_arr[l - 1]
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_l = l
                max_r = r
    print('max_sum: ',max_sum )
    print('l: ',max_l)
    print('r: ',max_r) 

arr = [-68 ,78 ,95 ,59 ,77 ,-89 ,-100 ,-48 ,68 ,28]
maxSubArray(arr)
'''