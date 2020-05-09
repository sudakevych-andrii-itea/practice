class Stack:
    def __init__(self, stack_size):
        self.stack = []
        self.stack_size = stack_size

    def __str__(self):
        return f'{self.stack}'

    def push(self, item):
        assert len(self.stack) < self.stack_size, 'Stack is overflowed'
        self.stack.append(item)

    def pop(self):
        assert len(self.stack), 'Stack is empty'
        return self.stack.pop()


if __name__ == '__main__':
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    stack.pop()
    print(stack)
