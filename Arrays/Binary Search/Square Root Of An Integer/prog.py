#Author: Rahil Sayed
#Date: 02/08/2021

'''
-----------------------------------------------------
Square Root Of Integer
-----------------------------------------------------
Implement int sqrt(int x).
Compute and return the square root of x.
If x is not a perfect square, return floor(sqrt(x))
-----------------------------------------------------
Example:
-----------------------------------------------------
Input : 11
Output : 3
-----------------------------------------------------
Warning: DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY
-----------------------------------------------------
'''
#Note:  Floor square root of a number is the greatest whole number which is less than or equal to its square root.


def sqrt(n):
    low = 1
    high = n
    mid = 0
    while low <= high:
        mid = high + low // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            low = mid + 1
        elif mid * mid > n:
            high = mid - 1
    return mid

print(sqrt(17))

#Output:
'''
4
'''

#Time Complexity: O(log(n))
#Space Complexity: O(1)