# Плюсы: автоматическое управление памятью
# Минусы: зависимость от стандартной библиотеки
from collections import deque


class CircularBufferV2:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def is_empty(self):
        return len(self.buffer) == 0

    def is_full(self):
        return len(self.buffer) == self.buffer.maxlen

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Buffer is full, cannot enqueue")
        self.buffer.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Buffer is empty, cannot dequeue")
        return self.buffer.popleft()
