#Author: Rahil Sayed
#Date: 10/05/2021

def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            position = i 
            return position

#sample test case
arr = [1,0,2,9,3,84,7,5,6]
key = 3
print(linear_search(arr,key)) 

'''
Output: 
4 
'''

#Time Complexity: O(n)
#Space Complexity: O(1) 