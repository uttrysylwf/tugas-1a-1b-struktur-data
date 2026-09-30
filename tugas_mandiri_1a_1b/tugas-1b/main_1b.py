from antrean import Antrean
from undo import Undo

antrean = Antrean()
undo = Undo()

# ===== SIMULASI ANTREAN (QUEUE) =====
# Langkah 1: is_empty (awal)
print("Kosong?", antrean.is_empty())

# Langkah 2: enqueue Andi
antrean.enqueue(1, "Andi")
print("Antrean:", antrean.daftar())

# Langkah 3: enqueue Siti
antrean.enqueue(2, "Siti")
print("Antrean:", antrean.daftar())

# Langkah 4: enqueue Budi
antrean.enqueue(3, "Budi")
print("Antrean:", antrean.daftar())

# Langkah 5: enqueue Dewi
antrean.enqueue(4, "Dewi")
print("Antrean:", antrean.daftar())

# Langkah 6: enqueue Rizky
antrean.enqueue(5, "Rizky")
print("Antrean:", antrean.daftar())

# Langkah 7: peek
print("Terdepan:", antrean.peek()[1])
print("Antrean:", antrean.daftar())

# Langkah 8: dequeue #1
print("Dilayani:", antrean.dequeue()[1])
print("Antrean:", antrean.daftar())

# Langkah 9: dequeue #2
print("Dilayani:", antrean.dequeue()[1])
print("Antrean:", antrean.daftar())

# Langkah 10: is_empty (akhir)
print("Kosong?", antrean.is_empty())
print("Antrean:", antrean.daftar())

# ===== SIMULASI UNDO (STACK) =====
print()

# Langkah 1: is_empty (awal)
print("Kosong?", undo.is_empty())

# Langkah 2: push 1
undo.push("30-09-2026 08:00", "Tambah Andi")
print("Stack:", undo.daftar())

# Langkah 3: push 2
undo.push("30-09-2026 08:10", "Ubah Siti")
print("Stack:", undo.daftar())

# Langkah 4: push 3
undo.push("30-09-2026 08:20", "Hapus Budi")
print("Stack:", undo.daftar())

# Langkah 5: push 4
undo.push("30-09-2026 08:30", "Cetak Dewi")
print("Stack:", undo.daftar())

# Langkah 6: push 5
undo.push("30-09-2026 08:40", "Status Rizky")
print("Stack:", undo.daftar())

# Langkah 7: peek
print("Puncak:", undo.peek()[1])
print("Stack:", undo.daftar())

# Langkah 8: pop #1
print("Dibatalkan:", undo.pop()[1])
print("Stack:", undo.daftar())

# Langkah 9: pop #2
print("Dibatalkan:", undo.pop()[1])
print("Stack:", undo.daftar())

# Langkah 10: is_empty (akhir)
print("Kosong?", undo.is_empty())
print("Stack:", undo.daftar())
