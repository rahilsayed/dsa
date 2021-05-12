#Author: Rahil Sayed
#Date: 11/05/2021

def tower_of_hanoi(discs, start, helper, destination):
    
    #base case
    if discs == 1:
        print(start + " to " + destination)
        return
    
    #resursive case
    #from start to helper
    tower_of_hanoi(discs - 1, start, destination, helper)
    #from start to destination
    print(start + " to " + destination)
    #from helper to destination
    tower_of_hanoi(discs - 1, helper, start, destination)

#sample test case
tower_of_hanoi(3,"A","B","C")

#Time Complexity: O(2^n) (Exponential)
#Space Complexity: O(n) (Linear)