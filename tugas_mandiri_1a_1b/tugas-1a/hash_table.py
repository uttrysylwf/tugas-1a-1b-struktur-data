class HashTable:
    """Hash table (dictionary Python): cari data lewat key (NIM)."""

    def __init__(self):
        self.tabel = {}

    def simpan(self, nim, mhs):  # rata-rata O(1)
        self.tabel[nim] = mhs

    def cari(self, nim):         # rata-rata O(1)
        return self.tabel.get(nim)

    def hapus(self, nim):        # rata-rata O(1)
        self.tabel.pop(nim, None)
