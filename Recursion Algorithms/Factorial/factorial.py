#Author: Rahil Sayed
#Date: 11/05/2021

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

#sample test case
print(factorial(10))

#Time Complexity: O(n) (Explained in notes)
#Space Complexity: O(n) (Explained in notes)