#Author: Rahil Sayed
#Date: 12/05/2021


class Stack:
    def __init__(self,size):
        self.data = []
        self.top = -1
        self.size = size

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def isFull(self):
        if self.top >= self.size:
            return True
        return False

    def peek(self):
        if self.isEmpty():
            return
        return self.data[self.top]

    def push(self,val):
        if self.isFull():
            return
        self.data.append(val)
        self.top += 1

    def pop(self):
        if self.isEmpty():
            return
        self.top -= 1
        return self.data.pop()

    def display(self):
        for i in self.data[::-1]:
            print(i)

def isBalanced(exp):
    s = Stack(len(exp))
    open_list = ['(','[','{']
    close_list = [')',']','}']
    for i in range(len(exp)):
        if exp[i] in open_list:
            s.push(exp[i])
        elif exp[i] in close_list:
            pos = close_list.index(exp[i])
            if s.peek() == open_list[pos]:
                s.pop()
            else:
                return False
    if s.isEmpty():
        return True
    else:
        return False


#sample test case
exp = input("Enter expression: ")
if isBalanced(exp):
    print("Balanced")
else:
    print("Not Balanced")