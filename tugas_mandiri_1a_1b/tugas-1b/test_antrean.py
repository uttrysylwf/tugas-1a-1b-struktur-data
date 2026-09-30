import unittest
from antrean import Antrean


class TestEnqueue(unittest.TestCase):
    def test_satu_data(self):
        a = Antrean()
        a.enqueue(1, "Andi")
        self.assertEqual(a.daftar(), ["Andi"])

    def test_lima_data(self):
        a = Antrean()
        a.enqueue(1, "Andi")
        a.enqueue(2, "Siti")
        a.enqueue(3, "Budi")
        a.enqueue(4, "Dewi")
        a.enqueue(5, "Rizky")
        self.assertEqual(a.daftar(), ["Andi", "Siti", "Budi", "Dewi", "Rizky"])


class TestDequeue(unittest.TestCase):
    def setUp(self):
        self.a = Antrean()
        self.a.enqueue(1, "Andi")
        self.a.enqueue(2, "Siti")
        self.a.enqueue(3, "Budi")

    def test_ambil_paling_depan(self):
        self.assertEqual(self.a.dequeue(), (1, "Andi"))
        self.assertEqual(self.a.daftar(), ["Siti", "Budi"])

    def test_urutan_fifo(self):
        self.a.dequeue()
        self.a.dequeue()
        self.assertEqual(self.a.dequeue(), (3, "Budi"))

    def test_antrean_kosong(self):
        self.assertIsNone(Antrean().dequeue())


class TestPeek(unittest.TestCase):
    def test_lihat_terdepan(self):
        a = Antrean()
        a.enqueue(1, "Andi")
        a.enqueue(2, "Siti")
        self.assertEqual(a.peek(), (1, "Andi"))
        self.assertEqual(a.daftar(), ["Andi", "Siti"])   # data tidak berkurang

    def test_setelah_dequeue(self):
        a = Antrean()
        a.enqueue(1, "Andi")
        a.enqueue(2, "Siti")
        a.dequeue()
        self.assertEqual(a.peek(), (2, "Siti"))

    def test_antrean_kosong(self):
        self.assertIsNone(Antrean().peek())


class TestIsEmpty(unittest.TestCase):
    def test_antrean_baru(self):
        self.assertTrue(Antrean().is_empty())

    def test_setelah_enqueue(self):
        a = Antrean()
        a.enqueue(1, "Andi")
        self.assertFalse(a.is_empty())

    def test_setelah_semua_dilayani(self):
        a = Antrean()
        a.enqueue(1, "Andi")
        a.dequeue()
        self.assertTrue(a.is_empty())


if __name__ == "__main__":
    unittest.main()
