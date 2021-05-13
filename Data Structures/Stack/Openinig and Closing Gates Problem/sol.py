#Author: Rahil Sayed
#Date: 13/05/2021


'''
A water reservation system constructed in a city has several opening and closing gates. If any opening gates are not closed with a corresponding closing gate then the water will leak out of the system and there will be a threat to the life of people living in the city. Also, the closing gate cannot exist without the opening gate, so the system head checks the design of the system and he has to ensure that the people are safe in the city. Write an algorithm to find whether people are safe or not.
'''


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


def check(gates):
    count = 0
    stack = Stack(len(gates))
    for gate in gates:
        if gate == '(':
            stack.push(gate)
        elif gate == ')':
            if not stack.isEmpty() and stack.peek() == '(':
                stack.pop()
                count += 1
            else:
                return -1
    if not stack.isEmpty():
        return -1
    else:
        return count


#sample test case
gates = '(())'
check_gates = check(gates)
if check_gates == -1:
    print("Not Secure")
else:
    print("Secure with {} gates".format(check_gates))