#Author: Rahil Sayed
#Date: 11/06/2021

'''
Give a unsorted list and a number n.
Return the number of occurrence of n.


#####Example:

#####Input:

A.  1->4->3->2->4
    n = 4
    
B.  1->9->4
    n = 3

#####Output:

A.  2
 
B.  0

'''


def search(head,n):
    temp = head
    count = 0
    while temp:
        if temp.data == n:
            count += 1
        temp = temp.next
    return count