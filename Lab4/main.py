# Problema 1
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def print(self):
        print(f'Current stack: {self.items}')

print("Problema 1")
print("")
stack = Stack()
stack.push(4)
stack.push(8)
stack.push(6)
stack.push(2)

stack.print()
stack.pop()
print(f'Peek : {stack.peek()}')
stack.pop()
stack.pop()
stack.print()
stack.pop()
print(stack.pop())
print("")

# Problema 2

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def print(self):
        print(f'Current queue: {self.items}')


print("Problema 2")
print("")
queue = Queue()
queue.push(3)
queue.push(1)
queue.push(7)
queue.push(9)
queue.push(5)

queue.print()
print(f'Peek : {queue.peek()}')
queue.pop()
queue.pop()
queue.print()
print(f'Peek : {queue.peek()}')
queue.pop()
queue.pop()
queue.pop()
print(queue.pop())
print("")

# Problema 3