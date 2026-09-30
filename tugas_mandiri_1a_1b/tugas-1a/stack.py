class Stack:
    """Stack (LIFO): yang terakhir masuk, pertama keluar. Untuk fitur Undo."""

    def __init__(self):
        self.items = []

    def push(self, data):        # O(1)
        self.items.append(data)

    def pop(self):               # O(1)
        return self.items.pop()

    def peek(self):              # O(1)
        return self.items[-1]

    def is_empty(self):          # O(1)
        return len(self.items) == 0
