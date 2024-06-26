# Плюсы: простота реализации, эффективное использование памяти.
# Минусы: неэффективные операции изменения размера.
# Скорость выполнения удаления и вставки в очередь O(1).
# Если сравнивать 1 и 2 варианты по скорости я склоняюсь к тому, что 2 будет
# быстрее, т.к библиотека реализована на более быстром языке C.
class CircularBufferV1:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Buffer is full, cannot enqueue")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Buffer is empty, cannot dequeue")
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item
