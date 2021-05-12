#Author: Rahil Sayed
#Date: 12/05/2021

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


class Fixes:
    def __init__(self,infix):
        self.infix = infix.strip()
        self.stack = Stack(len(self.infix))
        self.output = []
        self.precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}

    def isOperand(self,ch):
        return ch.isalnum()

    def notGreater(self,ch):
        try:
            a = self.precedence[ch]
            b = self.precedence[self.stack.peek()]
            if a <= b:
                return True
            else: return False
        except KeyError:
            return False

    def convert(self):
        for i in self.infix:
            if self.isOperand(i):
                self.output.append(i)

            elif i == '(':
                self.stack.push(i)

            elif i == ')':
                while not self.stack.isEmpty() and self.stack.peek() != '(':
                    x = self.stack.pop()
                    self.output.append(x)
                if not self.stack.isEmpty() and self.stack.peek() == '(':
                    self.stack.pop()
                else:
                    return -1

            else:
                while not self.stack.isEmpty() and self.notGreater(i):
                    self.output.append(self.stack.pop())
                self.stack.push(i)

        while not self.stack.isEmpty():
            self.output.append(self.stack.pop())

        self.postfix = "".join(self.output)


#sample test case       
infix = '(2+3)*7-9/2^1'
f = Fixes(infix)
f.convert()
print(f.postfix)