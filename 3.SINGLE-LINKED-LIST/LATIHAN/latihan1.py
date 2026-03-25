class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_awal(self, data):
        node_baru = Node(data)
        node_baru.next = self.head
        self.head = node_baru

    def insert_akhir(self, data):
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node_baru

    def tampilkan(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Pengujian
ll = LinkedList()
ll.insert_awal(10)
ll.insert_awal(20)
ll.insert_akhir(30)
ll.insert_akhir(40)

ll.tampilkan()