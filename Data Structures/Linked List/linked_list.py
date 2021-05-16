#Author: Rahil Sayed
#Date: 15/05/2021


#linked list data structure

#node class
class Node:

    def  __init__(self,data = None):
        self.data = data
        self.next = None


#linked list class
class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self,val):
        n = Node(val)
        if self.head == None:
            self.head = n
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = n

    def remove(self,val):
        temp = self.head
        if temp.data == val:
            self.head = temp.next
            return
        while temp.next:
            if temp.next.data == val:
                break
            else:
                temp = temp.next
        if not temp.next:
            return
        temp.next = temp.next.next

    def search(self,val):
        temp = self.head
        while temp:
            if temp.data == val:
                print('True')
                return
            temp = temp.next
        print('False')
        return

    def insertIndex(self,idx,val):
        n = Node(val)
        temp = self.head
        if idx == 0:
            n.next = temp
            self.head = n
            return
        #if inx is not 0 i.e head, then start iterating from 1, hence set a variable to 1
        temp_idx = 1
        #while temp_idx is one position before the target index position
        while temp_idx <= idx - 1 and temp:
            temp = temp.next
            temp_idx += 1
        if not temp:
            return
        n.next = temp.next
        temp.next = n

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next


#sample test case
ll = LinkedList()
ll.insert(7)
ll.insert(8)
ll.insert(6)
ll.insert(9)
ll.remove(9)
ll.search(9)
ll.insertIndex(3,0)
ll.display()