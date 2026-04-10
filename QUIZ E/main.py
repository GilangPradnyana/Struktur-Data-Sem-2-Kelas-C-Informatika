# =====================================================
# Quis 1 - Struktur Data: Array dan Linked List
# Nama : I Putu Gilang Pradnyana
# NIM  : [MASUKKAN NIM KAMU]
# Kelas: [MASUKKAN KELAS KAMU]
# =====================================================

class Node:
    """Class dasar untuk node pada Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    Implementasi Singly Linked List
    
    Karakteristik:
    - Setiap node hanya memiliki pointer ke node berikutnya
    - Akses elemen: O(n)
    - Insertion/Deletion di posisi tertentu (setelah diketahui node): O(1)
    """

    def __init__(self):
        """Inisialisasi Linked List kosong"""
        self.head = None
        self.size = 0

    def is_empty(self):
        """Cek apakah list kosong"""
        return self.head is None

    def append(self, data):
        """Menambahkan elemen di akhir list - O(n)"""
        new_node = Node(data)
        self.size += 1
        
        if self.is_empty():
            self.head = new_node
            return
            
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, position, data):
        """Menyisipkan elemen pada posisi tertentu - O(n)"""
        if position < 0 or position > self.size:
            raise IndexError("Posisi di luar batas")
            
        new_node = Node(data)
        self.size += 1
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
            
        current = self.head
        for _ in range(position - 1):
            current = current.next
            
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        """Menghapus node berdasarkan nilai data - O(n)"""
        if self.is_empty():
            return False
            
        # Jika head yang dihapus
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
            
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
            
        if current.next:
            current.next = current.next.next
            self.size -= 1
            return True
        return False

    def display(self):
        """Menampilkan seluruh isi list"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "List kosong")


class DoublyNode:
    """Node untuk Doubly Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    Implementasi Doubly Linked List
    
    Keunggulan dibanding Singly:
    - Bisa traversal maju dan mundur
    - Deletion lebih mudah (O(1) jika node sudah diketahui)
    - Menggunakan memori lebih besar (ada pointer prev)
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        """Tambah di akhir - O(1)"""
        new_node = DoublyNode(data)
        self.size += 1
        
        if self.head is None:
            self.head = self.tail = new_node
            return
            
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def display_forward(self):
        """Tampilkan dari depan ke belakang"""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements) if elements else "List kosong")

    def display_backward(self):
        """Tampilkan dari belakang ke depan"""
        current = self.tail
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
        print(" <-> ".join(elements) if elements else "List kosong")


class CircularLinkedList:
    """
    Implementasi Circular Singly Linked List
    
    Perbedaan utama: node terakhir menunjuk kembali ke head
    Cocok untuk: Round-Robin Scheduling, playlist berulang, dll.
    """

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        """Tambah elemen di akhir (membuat circular)"""
        new_node = Node(data)
        self.size += 1
        
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
            
        current = self.head
        while current.next != self.head:
            current = current.next
            
        current.next = new_node
        new_node.next = self.head

    def display(self):
        """Tampilkan isi circular list"""
        if not self.head:
            print("List kosong")
            return
            
        elements = []
        current = self.head
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        print(" -> ".join(elements) + " -> (back to start)")


# ====================== DEMO PROGRAM ======================
if __name__ == "__main__":
    print("="*60)
    print("QUIS 1 - DEMO IMPLEMENTASI STRUKTUR DATA")
    print("="*60)
    
    # 1. Dynamic Array (Python List)
    print("\n1. Dynamic Array (Python List):")
    arr = []
    for i in range(1, 6):
        arr.append(i)
    print("Array:", arr)
    print("Akses indeks 2:", arr[2], "(O(1))")
    
    # 2. Singly Linked List
    print("\n2. Singly Linked List:")
    sll = SinglyLinkedList()
    for i in [10, 20, 30, 40]:
        sll.append(i)
    sll.display()
    sll.insert(2, 25)
    print("Setelah insert 25 di posisi 2:")
    sll.display()
    
    # 3. Doubly Linked List
    print("\n3. Doubly Linked List:")
    dll = DoublyLinkedList()
    for i in [100, 200, 300, 400]:
        dll.append(i)
    dll.display_forward()
    print("Traversal mundur:")
    dll.display_backward()
    
    # 4. Circular Linked List
    print("\n4. Circular Linked List:")
    cll = CircularLinkedList()
    for i in [1, 2, 3, 4, 5]:
        cll.append(i)
    cll.display()
    
    print("\n" + "="*60)
    print("Semua struktur data telah diimplementasikan dengan dokumentasi.")
    print("Silakan copy kode ini ke repository kamu.")
    print("="*60)