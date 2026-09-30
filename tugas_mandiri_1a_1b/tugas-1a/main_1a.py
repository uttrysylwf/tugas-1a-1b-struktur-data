from array_list import DaftarArray
from linked_list import LinkedList
from stack import Stack
from antrean import Queue
from hash_table import HashTable
from tree import TreeNode

# Data mahasiswa
data = [
    {"nim": "12250001", "nama": "Andi", "prodi": "Teknik Informatika"},
    {"nim": "12250002", "nama": "Siti", "prodi": "Sistem Informasi"},
    {"nim": "12250003", "nama": "Budi", "prodi": "Teknik Informatika"},
    {"nim": "12250004", "nama": "Dewi", "prodi": "Teknik Industri"},
]

print("=== 1. ARRAY: penyimpanan data berurutan ===")
arr = DaftarArray()
for m in data:
    arr.tambah(m)
print("Data indeks ke-2 :", arr.ambil(2)["nama"])
print("Cari 12250004    : indeks", arr.cari("12250004"))

print("\n=== 2. LINKED LIST: tambah/hapus dinamis ===")
ll = LinkedList()
for m in data:
    ll.tambah_belakang(m)
ll.tambah_depan({"nim": "12250000", "nama": "Rina", "prodi": "Teknik Informatika"})
print("Setelah tambah depan :", ll.daftar_nama())
ll.hapus("12250002")
print("Setelah hapus Siti   :", ll.daftar_nama())

print("\n=== 3. STACK: fitur Undo (LIFO) ===")
undo = Stack()
undo.push("Tambah Andi")
undo.push("Ubah Siti")
undo.push("Hapus Budi")
print("Undo pertama  :", undo.pop())
print("Undo kedua    :", undo.pop())
print("Stack kosong? :", undo.is_empty())

print("\n=== 4. QUEUE: antrean pengolahan data (FIFO) ===")
antre = Queue()
antre.enqueue("Andi")
antre.enqueue("Siti")
antre.enqueue("Budi")
print("Diproses pertama :", antre.dequeue())
print("Diproses kedua   :", antre.dequeue())
print("Antrean kosong?  :", antre.is_empty())

print("\n=== 5. HASH TABLE: pencarian berdasarkan key (NIM) ===")
ht = HashTable()
for m in data:
    ht.simpan(m["nim"], m)
hasil = ht.cari("12250003")
print("Cari 12250003 :", hasil["nama"], "-", hasil["prodi"])
print("Cari 99999999 :", ht.cari("99999999"))

print("\n=== 6. TREE: data hierarkis ===")
univ = TreeNode("UIN Suska Riau")
fst = univ.tambah_anak(TreeNode("Fakultas Sains dan Teknologi"))
ti = fst.tambah_anak(TreeNode("Teknik Informatika"))
ti.tambah_anak(TreeNode("Andi"))
ti.tambah_anak(TreeNode("Budi"))
si = fst.tambah_anak(TreeNode("Sistem Informasi"))
si.tambah_anak(TreeNode("Siti"))
univ.cetak()
