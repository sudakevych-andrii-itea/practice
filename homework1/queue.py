class Queue:
    def __init__(self, queue_size):
        self.queue = []
        self.queue_size = queue_size

    def __str__(self):
        return f'{self.queue}'

    def push(self, item):
        assert len(self.queue) < self.queue_size, 'Queue is overflowed'
        self.queue.append(item)

    def pop(self):
        assert len(self.queue), 'Queue is empty'
        return self.queue.pop(0)
