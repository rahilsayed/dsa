#Author: Rahil Sayed
#Date: 21/05/2021

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


#sample test case
if __name__ == "__main__":
    size = int(input("Enter Stack Size: "))
    s = Stack(size)
    print("\nEmpty Stack of size " + str(size) + " created\n")
    print("Stack Operations: \n \t 1. Push \n \t 2. Pop \n \t 3. Display \n \t 4. Exit")
    while True:
        op = int(input("\nEnter your choice: "))
        if op == 1:
            val = int(input("Enter the Value to push: "))
            s.push(val)
        elif op == 2:
            print(str(s.pop()) + " popped from the stack")
            
        elif op == 3:
            s.display()
        elif op == 4:
            break
        
