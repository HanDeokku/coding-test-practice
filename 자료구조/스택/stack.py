class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):
        return len(self.top) == 0

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop()

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    
    def size(self): return len(self.top)

    def clear(self): 
        self.top = []

s = Stack()

print(s.push(1))
print(s.push(2))
print(s.push(3))
print(s.pop())
print(s.pop())
print(s.size())
print(s.peek())
print(s.clear())
print(s.size())
