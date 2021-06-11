#Author: Rahil Sayed
#Date: 11/06/2021

'''
You’re given the pointer to the head nodes of two sorted linked lists.
The data in both lists will be sorted in ascending order. Change the next pointers to obtain a single, merged linked list which also has data in ascending order.

Return the head of this merged list.

#####Example :

#####Input :
(head1) 1->2->3->5->null
(head2) 3->4->6->null

#####Output :
(head) 1->2->3->3->4->5->6->null
'''

def mergeSort_ll(head1,head2):
    #base case
    if head1 == None:
        return head2
    elif head2 == None:
        return head1

    #recursive case
    if head1.data <= head2.data:
        result = head1
        result.next = mergeSort_ll(head1.next,head2)
    else:
        result = head2
        result.next = mergeSort_ll(head1,head2.next)

    return result


