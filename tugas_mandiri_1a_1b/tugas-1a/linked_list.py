class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Linked list: tambah/hapus data tanpa menggeser elemen lain."""

    def __init__(self):
        self.head = None

    def tambah_depan(self, data):        # O(1)
        node = Node(data)
        node.next = self.head
        self.head = node

    def tambah_belakang(self, data):     # O(n)
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def hapus(self, nim):                # O(n)
        cur = self.head
        prev = None
        while cur is not None:
            if cur.data["nim"] == nim:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return True
            prev = cur
            cur = cur.next
        return False

    def daftar_nama(self):
        hasil = []
        cur = self.head
        while cur is not None:
            hasil.append(cur.data["nama"])
            cur = cur.next
        return hasil
