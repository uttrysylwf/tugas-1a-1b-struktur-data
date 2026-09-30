import unittest
from undo import Undo


class TestPush(unittest.TestCase):
    def test_satu_aktivitas(self):
        u = Undo()
        u.push("30-09-2026 08:00", "Tambah Andi")
        self.assertEqual(u.daftar(), ["Tambah Andi"])

    def test_lima_aktivitas(self):
        u = Undo()
        u.push("30-09-2026 08:00", "Tambah Andi")
        u.push("30-09-2026 08:10", "Ubah Siti")
        u.push("30-09-2026 08:20", "Hapus Budi")
        u.push("30-09-2026 08:30", "Cetak Dewi")
        u.push("30-09-2026 08:40", "Status Rizky")
        self.assertEqual(u.peek()[1], "Status Rizky")
        self.assertEqual(len(u.daftar()), 5)


class TestPop(unittest.TestCase):
    def setUp(self):
        self.u = Undo()
        self.u.push("30-09-2026 08:00", "Tambah Andi")
        self.u.push("30-09-2026 08:10", "Ubah Siti")
        self.u.push("30-09-2026 08:20", "Hapus Budi")

    def test_batalkan_terakhir(self):
        self.assertEqual(self.u.pop()[1], "Hapus Budi")
        self.assertEqual(self.u.daftar(), ["Tambah Andi", "Ubah Siti"])

    def test_urutan_lifo(self):
        self.u.pop()
        self.u.pop()
        self.assertEqual(self.u.pop()[1], "Tambah Andi")

    def test_stack_kosong(self):
        self.assertIsNone(Undo().pop())


class TestPeek(unittest.TestCase):
    def test_lihat_puncak(self):
        u = Undo()
        u.push("30-09-2026 08:00", "Tambah Andi")
        u.push("30-09-2026 08:10", "Ubah Siti")
        self.assertEqual(u.peek()[1], "Ubah Siti")
        self.assertEqual(len(u.daftar()), 2)             # data tidak berkurang

    def test_setelah_pop(self):
        u = Undo()
        u.push("30-09-2026 08:00", "Tambah Andi")
        u.push("30-09-2026 08:10", "Ubah Siti")
        u.pop()
        self.assertEqual(u.peek()[1], "Tambah Andi")

    def test_stack_kosong(self):
        self.assertIsNone(Undo().peek())


class TestIsEmpty(unittest.TestCase):
    def test_stack_baru(self):
        self.assertTrue(Undo().is_empty())

    def test_setelah_push(self):
        u = Undo()
        u.push("30-09-2026 08:00", "Tambah Andi")
        self.assertFalse(u.is_empty())

    def test_setelah_semua_dibatalkan(self):
        u = Undo()
        u.push("30-09-2026 08:00", "Tambah Andi")
        u.pop()
        self.assertTrue(u.is_empty())


if __name__ == "__main__":
    unittest.main()
