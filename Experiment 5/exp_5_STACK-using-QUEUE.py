from collections import deque

class Stack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)

    def pop(self):
        if self.q:
            for i in range(len(self.q) - 1):
                self.q.append(self.q.popleft())
            return self.q.popleft()
        return "Stack is empty"

    def top(self):
        if self.q:      
            return self.q[-1]
        return "Stack is empty"


s = Stack()

s.push(1)
s.push(2)
s.push(3)

print(s.top())   
print(s.pop())   
print(s.pop())   
print(s.pop())   