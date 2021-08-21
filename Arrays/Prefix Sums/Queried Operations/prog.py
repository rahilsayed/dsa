#Author: Rahil Sayed
#Date: 26/07/2021


'''
--------------------------------------------------
Queried Operations
--------------------------------------------------
Given an Array A, with n elements and also a set of Q queries.
Each query contains L and R and V. Your task is to add V for all indexes from L to R, both inclusive.
Finally, print the array after all Q queries.
--------------------------------------------------
Constraints:
--------------------------------------------------
1 <= N <= 10^6
1 <= Q <= 10^6
1 <= L, R, <= N
--------------------------------------------------
Input format:
--------------------------------------------------
First line contains N, followed by N elements of the array
Next line contains Q, the number of queries
This is followed by Q lines, each containing the respective L, R and V
--------------------------------------------------
Output format:
--------------------------------------------------
Print the array in a single line after all queries are completed.
--------------------------------------------------
'''


def incrementByV(arr,q_arr,n,m):

    #create an auxillary array for bucketing
    sum = [0 for i in range(n)]

    #loop in the range of m
    for i in range(m):

        #Add at position q_arr[i][0] i.e the starting range number (l i.e first element) of sum array, a value of q_arr[i][-1] i.e the V (increment value i.e last element) 

        sum[q_arr[i][0]] += q_arr[i][-1]  

        #Now, Subtract at position q_arr[i][1] + 1 i.e the ending range number + 1 (r i.e the second element + 1), a value of negative q_arr[i][-1] i.e the V (increment value i.e last element) ONLY IF q_arr[i][1] + 1 EXISTS.
        
        if (q_arr[i][1] + 1) < n:
            sum[q_arr[i][1] + 1] -= q_arr[i][-1]

        #Now, accumulate the value in the sum[] itself to create a consecutive array.
        # The add them to the CORRESPONDING indexes in arr[]
        #Assign the first element as it is

    arr[0] += sum[0]
    for i in range(1,n):
        sum[i] += sum[i - 1]
        arr[i] += sum[i]

    return arr

arr = list(map(int,input().split()))
N = arr[0]
arr = arr[1:]
Q = int(input())
Q_arr = [None] * Q
for i in range(Q):
    Q_arr[i] = list(map(int,input().split()))
arr = incrementByV(arr, Q_arr, len(arr), len(Q_arr))
for i in arr:
    print(i,end=' ')

#Sample Test Case:
'''
10 46 20 7 -9 -2 45 18 47 4 67
5
1 9 3
2 6 7
2 8 -3
4 7 15
1 6 -4 
'''

#Output:
'''
46 19 10 -6 16 63 36 62 4 70
'''

#Time Complexity: O(N + Q)