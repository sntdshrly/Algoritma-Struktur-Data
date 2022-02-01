'''
sherly santiadi
2072025
uas algoritma dan struktur data
'''

from multiprocessing.sharedctypes import Value

'''
Soal 1.
- Buatlah class QueueElement yang memiliki atribut value dan next.
- Buatlah class Queue yang memiliki atribut head dan length (panjang antrian) serta method enqueue(value) untuk menambahkan antrian dan dequeue() untuk menghapus antrian dan mengembalikan nilai dari elemen yang dihapus.
- Override method str dari class Queue agar dapat menampilkan isi dari Queue tersebut.
- Gunakan fungsi main untuk menguji apakah pekerjaaan kalian sudah benar atau belum.
'''

class Queue:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        result = ""
        pointer = self.head
        self.length = 0
        while pointer != None: # supaya berhenti di None
            result = result + str(pointer.value) + " "
            pointer = pointer.next
            self.length += 1
        return result

    def enqueue(self,value):
        e = QueueElement(value)
        pointer = self.head

        if self.head == None:
            self.head = e
        else:
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = e
        self.length += 1

    def dequeue(self):
        pointer = self.head
        self.head = pointer.next
        pointer.next = None
        self.length -= 1
        return pointer.value

class QueueElement:
    def __init__(self,  value, next = None):
        self.value = value
        self.next = next


'''
Soal 2.
- Buatlah sebuah class DoubleLinkedListElement yang memiliki atribut next, prev, dan value.
- Buatlah sebuah class DoubleLinkedList yang memiliki atribut head, tail, dan count (jumlah element dalam double linked list) serta method addFirst(value) untuk menambahkan element pada awal double linked list dan method removeIndex(idx) untuk menghapus elemen yang index ke idx. Method removeIndex(idx) akan mengembalikan value dari elemen yang dihapus tersebut.
- Override method str dari class DoubleLinkedList agar menampilkan isi DoubleLinkedList dari belakang ke depan.
'''
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def printForward(self):
        pointer = self.head

        while pointer != None:
            print(pointer.value, end=" ")
            pointer = pointer.next

    def printBackward(self):
        pointer = self.tail

        while pointer != None:
            print(pointer.value, end=" ")
            pointer = pointer.prev

    def addFirst(self, value):
        e = DoubleLinkedListElement(value)
        if self.head == None:
            e.next = None
            e.prev = None
            self.head = e
            self.tail = e
        else:
            self.head.prev = e
            e.next = self.head
            self.head = e
        self.count += 1

    def removeFirst(self):
        pointer = self.head

        self.head = pointer.next
        self.head.prev = None
        pointer.next = None
        self.count -= 1
        return pointer.value

    def removeLast(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def removeIndex(self, index):
        pointer = self.head
        if index <= 0:
            return self.removeFirst()
        elif index >= self.count-1:
            return self.removeLast()
        else:
            pointer = self.head
            selectedIndex = 0
            while selectedIndex != index-1:  # mencari yg sebelum index
                pointer = pointer.next
                selectedIndex += 1
            pointer.next.next.prev = pointer
            # pointer sekarang nunjuk yang sebelum mau dihapus
            temp = pointer.next
            pointer.next = temp.next
            temp.next = None
            temp.prev = None
            self.count -= 1
            return temp.value

class DoubleLinkedListElement:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def main():
    '''
    Bagian ini adalah def main untuk pengujian nomor 1
    '''
    x = Queue()
    e5 = QueueElement(5)
    e4 = QueueElement(4, next= e5)
    e3 = QueueElement(3, next= e4)
    e2 = QueueElement(2, next= e3)
    e1 = QueueElement(1, next= e2)
    x.head = e1

    '''
    untuk mencetak queue sebelum ditambahkan
    '''
    print(x)
    print(x.length)

    '''
    untuk mencetak queue setelah ditambahkan data dummy, cek juga length-nya
    '''
    x.enqueue(999)
    x.enqueue(9999)
    print(x)
    print(x.length)

    '''
    untuk mencetak queue setelah di-dequeue, cek juga length-nya
    '''
    x.dequeue()
    print(x)
    print(x.length)

    # '''
    # Bagian ini adalah def main untuk pengujian nomor 2
    # '''
    # y = DoubleLinkedList()
    # y.addFirst(5)
    # y.addFirst(4)
    # y.addFirst(3)
    # y.addFirst(2)
    # y.addFirst(1)

    # '''
    # buka komentar untuk cek count-nya
    # '''
    # # print(y.count)

    # '''
    # buka komentar untuk mengecek 3 kondisi
    # 1. remove index awal
    # 2. remove index di tengah-tengah list
    # 3. remove index akhir
    # '''
    # # y.removeIndex(0)
    # # y.removeIndex(1)
    # # y.removeIndex(4)

    # '''
    # method cetak ke layar dari belakang ke depan (backward)
    # '''
    # print("print backward: ")
    # y.printBackward()

    # '''
    # buka komentar untuk mencoba method cetak ke layar dari depan ke belakang (forward)
    # '''
    # # print("print forward: ")
    # # y.printForward()

main()
