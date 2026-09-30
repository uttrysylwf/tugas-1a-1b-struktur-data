from collections import deque


class Antrean:
    """Queue (FIFO): masuk dari belakang, keluar dari depan."""

    def __init__(self):
        self.data = deque()

    def enqueue(self, nomor, nama):      # tambah di belakang -> O(1)
        self.data.append((nomor, nama))

    def dequeue(self):                   # layani yang paling depan -> O(1)
        if self.is_empty():
            return None
        return self.data.popleft()

    def peek(self):                      # lihat yang paling depan -> O(1)
        if self.is_empty():
            return None
        return self.data[0]

    def is_empty(self):                  # cek antrean kosong -> O(1)
        return len(self.data) == 0

    def daftar(self):                    # daftar nama dari depan ke belakang
        return [nama for nomor, nama in self.data]
