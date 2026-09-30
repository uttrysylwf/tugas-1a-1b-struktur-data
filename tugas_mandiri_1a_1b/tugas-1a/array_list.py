class DaftarArray:
    """Array (list Python): data tersimpan berurutan."""

    def __init__(self):
        self.data = []

    def tambah(self, mhs):           # sisip di akhir     -> O(1)
        self.data.append(mhs)

    def ambil(self, indeks):         # akses lewat indeks -> O(1)
        return self.data[indeks]

    def cari(self, nim):             # linear search      -> O(n)
        for i in range(len(self.data)):
            if self.data[i]["nim"] == nim:
                return i
        return -1

    def hapus(self, indeks):         # elemen digeser     -> O(n)
        return self.data.pop(indeks)
