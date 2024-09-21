#Program to implement Stack using List DS

import sys
class Stack:
        def __init__(self, size = 5):
                self.stk = [] #create an empty list to impliment the Stack
                self.sp = -1 #Consider the Stack empty at biginning of the program
                self.size = size
                print("An empty Stack of size ", size, " is created")

        def push(self):
                if self.sp == self.size-1:
                        print("Stack is full")
                        return
                self.sp += 1
                self.stk.append(input("Enter data to be pushed: "))
                # element = input("Enter data to be pushed: ")
                # self.stk.insert(sp, element)

        def pop(self):
                if len(self.stk) == 0:  # sp == -1
                        print("Stack is empty")
                        return
                print("Popped element is ", self.stk.pop())
                self.sp -= 1

        def displayStk(self):
                if self.sp == -1:
                        print("Stack is empty")
                        return
                print("Stack elements are: ", self.stk[::-1])

def invalid_choice():
        print("Invalid operation")

obj = Stack(4)
stk_oprs = {
        1 : obj.push,
        2 : obj.pop,
        3 : obj.displayStk,
        4 : sys.exit
}
choice = 0
while True:
        print("\n1:Push 2:Pop 3:Display-Stack 4:Exit")
        choice = int(input("Enter your choice: "))
        stk_oprs.get(choice, invalid_choice)()