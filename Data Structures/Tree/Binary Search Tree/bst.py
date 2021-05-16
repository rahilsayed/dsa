#Author: Rahil Sayed
#Date: 16/05/2021


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def search(self,val):
        if val < self.data:
            if self.left is None:
                print(False)
                return
            return self.left.search(val)
        elif val > self.data:
            if self.right is None:
                print(False)
                return
            return self.right.search(val)
        elif self.data == val:
            print(True)
            return
    
    def display_inorder(self):
        if self.left:
            self.left.display_inorder()
        print(self.data)
        if self.right:
            self.right.display_inorder()

    def display_preorder(self):
        print(self.data)
        if self.left:
            self.left.display_preorder()
        if self.right:
            self.right.display_preorder()

    def display_postorder(self):
        if self.left:
            self.left.display_postorder()
        print(self.data)
        if self.right:
            self.right.display_postorder()


#sample test case
root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
root.search(10)
root.display_inorder()
print('\n')
root.display_preorder()
print('\n')
root.display_postorder()
print('\n')