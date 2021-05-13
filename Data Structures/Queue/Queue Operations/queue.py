#Author: Rahil Sayed
#Date: 13/05/2021


#queue data structure
class Queue:
    def __init__(self,size):
        self.queue = []
        self.size = size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.rear == self.size - 1:
            return True
        else:
            return False

    def push(self,val):
        if not self.isFull():
            if self.front == -1:
                self.front += 1
            self.rear += 1
            self.queue.append(val)
            return True
        else:
            return False
    
    def pop(self):
        if not self.isEmpty():
            if self.front == self.rear:
                self.front -= 1
                self.rear -= 1
            else:
                self.front += 1
            return self.queue.pop(0)
        else:
            return False

    def peek(self):
        return self.front

    def display(self):
        for i in self.queue:
            print(i)


#sample test case
if __name__ == "__main__":
    size = int(input("Enter Queue Size: "))
    queue = Queue(size)
    print("\nEmpty Queue of size " + str(size) + " created\n")
    print("Queue Operations: \n \t 1. Push \n \t 2. Pop \n \t 3. Display \n \t 4. Exit")
    while True:
        op = int(input("\nEnter your choice: "))
        if op == 1:
            val = int(input("Enter the Value to push: "))
            if not queue.push(val):
                print("Cannot Add {}. Queue is Full".format(val))
        elif op == 2:
            popped = queue.pop()
            if popped is False:
                print("Queue is already empty")
            else:
                print("{} popped from the queue".format(popped))            
        elif op == 3:
            queue.display()
        elif op == 4:
            break

