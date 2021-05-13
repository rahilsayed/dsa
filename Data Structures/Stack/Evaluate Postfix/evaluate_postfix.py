#Author: Rahil Sayed
#Date: 13/05/2021


#stack data structure
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


#postfix evaluate function
def evaluate(exp):
    stack = Stack(len(exp))
    for i in exp:
        #if i is operand i.e int
        try:
            stack.push(int(i))
        #if i is operator
        except ValueError:
            num2 = stack.pop()
            num1 = stack.pop()
            switcher = {'+': num1 + num2, '-': num1 - num2, '*': num1 * num2, '/': num1 / num2}
            stack.push(switcher.get(i))
    return int(stack.pop())


#sample test case
exp = '30 400 * 15 60 * +'
exp = exp.split(" ")
print(evaluate(exp))
