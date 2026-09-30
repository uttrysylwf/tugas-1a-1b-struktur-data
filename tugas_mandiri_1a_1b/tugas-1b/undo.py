class Undo:
    """Stack (LIFO): aktivitas terakhir dibatalkan lebih dulu."""

    def __init__(self):
        self.data = []

    def push(self, waktu, aktivitas):    # simpan di puncak -> O(1)
        self.data.append((waktu, aktivitas))

    def pop(self):                       # batalkan yang terakhir -> O(1)
        if self.is_empty():
            return None
        return self.data.pop()

    def peek(self):                      # lihat puncak -> O(1)
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):                  # cek stack kosong -> O(1)
        return len(self.data) == 0

    def daftar(self):                    # daftar aktivitas dari dasar ke puncak
        return [aktivitas for waktu, aktivitas in self.data]
