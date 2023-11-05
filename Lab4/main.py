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

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.cell = [[0 for _ in range(m)] for _ in range(n)]

    def get(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.m:
            return self.cell[i][j]
        else:
            return None

    def set(self, i, j, value):
        if 0 <= i < self.n and 0 <= j < self.m:
            self.cell[i][j] = value

    def transpose(self):
        transposed = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transposed.cell[j][i] = self.cell[i][j]
        return transposed

    def multiply(self, other_matrix):
        if self.m != other_matrix.n:
            return None
        result = Matrix(self.n, other_matrix.m)
        for i in range(self.n):
            for j in range(other_matrix.m):
                for k in range(self.m):
                    result.cell[i][j] += self.cell[i][k] * other_matrix.cell[k][j]
        return result

    def function(self, transformation):
        for i in range(self.n):
            for j in range(self.m):
                self.cell[i][j] = transformation(self.cell[i][j])

    def print(self):
        for row in self.cell:
            print(row)

print("Problema 3")
print("")

matrix1 = Matrix(2, 4)
matrix1.set(0, 0, 1)
matrix1.set(0, 1, 2)
matrix1.set(0, 2, 3)
matrix1.set(0, 3, 4)
matrix1.set(1, 0, 5)
matrix1.set(1, 1, 6)
matrix1.set(1, 2, 7)
matrix1.set(1, 3, 8)

matrix2 = Matrix(4, 2)
matrix2.set(0, 0, 9)
matrix2.set(0, 1, 10)
matrix2.set(1, 0, 11)
matrix2.set(1, 1, 12)
matrix2.set(2, 0, 13)
matrix2.set(2, 1, 14)
matrix2.set(3, 0, 15)
matrix2.set(3, 1, 16)

print("Matrix 1:")
matrix1.print()

print("Matrix 2:")
matrix2.print()

result = matrix1.multiply(matrix2)
print("Multiplication:")
if result is None:
    print("The matrixes have different dimensions.")
else :
    result.print()

transposed = matrix1.transpose()
print("Transpose:")
transposed.print()

matrix1.function(lambda x: x + 5)
print("Transformation:")
matrix1.print()
