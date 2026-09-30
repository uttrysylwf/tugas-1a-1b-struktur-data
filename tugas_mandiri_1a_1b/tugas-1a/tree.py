class TreeNode:
    """Tree: data berbentuk hierarki (Fakultas > Prodi > Mahasiswa)."""

    def __init__(self, nama):
        self.nama = nama
        self.anak = []

    def tambah_anak(self, node):
        self.anak.append(node)
        return node

    def cetak(self, level=0):
        print("   " * level + "- " + self.nama)
        for a in self.anak:
            a.cetak(level + 1)
