#Author: Rahil Sayed
#Date: 02/08/2021

'''
-----------------------------------------------------
Implement Power Function
-----------------------------------------------------
Implement pow(x, n) % d .
In other words, given x, n and d,
find (x^n % d)
-----------------------------------------------------
Note: remainders on division cannot be negative. In other words, make sure the answer you return is non negative.
-----------------------------------------------------
Input : x = 2, n = 3, d = 3
Output : 2
 
2^3 % 3 = 8 % 3 = 2
-----------------------------------------------------
'''

def pow(a,b,p):
        if a == 0:
            return 0
        
        res = 1
        while b > 0:
            if b & 1:
                res = (res * a) % p
            b = b // 2
            a = (a * a) % p
        return (p + res) % p

#Sample Test Case
print(pow(20,5,3))

#Output:
'''
2
'''

#Time Complexity: O(log(n))
#Space Complexity: O(1)