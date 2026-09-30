from collections import deque


class Queue:
    """Queue (FIFO): yang pertama masuk, pertama keluar. Untuk antrean data."""

    def __init__(self):
        self.items = deque()

    def enqueue(self, data):     # O(1)
        self.items.append(data)

    def dequeue(self):           # O(1)
        return self.items.popleft()

    def is_empty(self):          # O(1)
        return len(self.items) == 0
