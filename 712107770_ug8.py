class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru

class Kasir:
    DEFAULT_CAPACITY = 3
    
    def __init__(self):
        self._data = [None] * Kasir.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Antrian sedang kosong")
        namaPelanggan = self._data[self._front].getNamaPelanggan()
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return namaPelanggan
    
    def enqueue(self, namaPelanggan):
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        posisi = (self._front + self._size) % len(self._data)
        self._data[posisi] = NodePelanggan(namaPelanggan)
        self._size += 1
    
    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
    
    def printAll(self):
        if self.is_empty():
            print("Antrian sedang kosong")
        else:
            walk = self._front
            for k in range(self._size):
                print(self._data[walk].getNamaPelanggan(), end=" ")
                walk = (1 + walk) % len(self._data)
            print()
        
# Inisialisasi kasir
print("=== Kasir ===")
kasir = Kasir()

# Menambahkan pelanggan ke antrian
kasir.enqueue("Haniif")
kasir.enqueue("Sindu")
kasir.enqueue("Dedi")

# Mencetak isi antrian kasir
kasir.printAll()

# Pelanggan pertama selesai membayar
print("Pelanggan Haniif Selesai Membayar")
kasir.dequeue()
print("=== Kasir ===")

# Melakukan resize pada kasir
print("* Melakukan Resize *")
print("=== Kasir ===")
kasir.enqueue("Beatrix")
kasir.enqueue("Kosong")
kasir.enqueue("Kosong")

# Mencetak isi antrian kasir setelah resize
kasir.printAll()

# Pelanggan kedua selesai membayar
print("Pelanggan Sindu Selesai Membayar")
print("=== Kasir ===")
kasir.dequeue()

# Mencetak isi antrian kasir setelah pelanggan selesai membayar
kasir.printAll()

# Menambahkan pelanggan baru ke antrian setelah resize
kasir.enqueue("Shalom")
print("=== Kasir ===")

# Mencetak isi antrian kasir setelah menambahkan pelanggan baru
kasir.printAll()
        


# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

