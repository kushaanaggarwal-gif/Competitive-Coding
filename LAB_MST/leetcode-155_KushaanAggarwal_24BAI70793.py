#leetcode problem 155

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    #adding element to the stack and checking if it is the minimum element
    def push(self, val):
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    #removing the top element from the stack
    def pop(self):
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    #checking the top element of the stack
    def top(self):
        return self.stack[-1]

    #checking the minimum element in the stack
    def getMin(self):
        return self.minStack[-1]

s = MinStack()

s.push(5)
s.push(3)
s.push(7)
s.push(2)

print("Top:", s.top())
print("Minimum:", s.getMin())

s.pop()

print("After pop:")
print("Top:", s.top())
print("Minimum:", s.getMin())    