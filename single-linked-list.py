class List:
    # head adalah ListElement (untuk menunjuk elemen awal di list)
    # pada awalnya, head tidak menunjuk elemen apapun
    
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        result = ""
        pointer = self.head

        while pointer != None: # supaya berhenti di None
            result = result + str(pointer.value) + " "
            pointer = pointer.next
        return result
    
    def addLast(self,value):
        e = ListElement(value)
        if self.head == None:
            self.head = e
        else:
            pointer = self.head
            while pointer.next != None: # supaya tidak berhenti di None
                pointer = pointer.next
            pointer.next = e
        self.length += 1

    def addFirst(self,value):
        e = ListElement(value)
        e.next = self.head
        self.head = e
        self.length += 1

    def insertData(self,value,index):
        e = ListElement(value)
        pointer = self.head
        
        if index > 1 and index <= self.length:
            while (index>1):
                pointer = pointer.next
                index = index-1
            temp = pointer.next
            pointer.next = e
            pointer.next.next = temp
        
        elif index <= 1:
            e = ListElement(value)
            e.next = self.head
            self.head = e
        
        elif index > 1 and index > self.length:
            e = ListElement(value)
            if self.head == None:
                self.head = e
            else:
                pointer = self.head
                while pointer.next != None:
                    pointer = pointer.next
                pointer.next = e
        
        self.length += 1

    def removeFirst(self):
        pointer = self.head
        self.head = pointer.next
        pointer.next = None
        self.length -= 1
        return pointer.value
    
    def removeLast(self):
        pointer = self.head
        while pointer.next.next != None:
            pointer = pointer.next.next
            pointer.next = None
            self.length -= 1
            return pointer.value
    
    def removeIndex(self, index):
        pointer = self.head

        if index > 1 and index <= self.length:
            while (index > 1):
                pointer = pointer.next
                index -= 1
            temp = pointer.next
            pointer.next = pointer.next.next
            temp.next = None
        elif index <=1:
            pointer = self.head
            self.head = pointer.next
            pointer.next = None
            self.length -= 1
            return pointer.value
        elif index > 1 and index > self.length:
            while pointer.next.next != None:
                pointer = pointer.next.next
                pointer.next = None
                self.length -= 1
                return pointer.value
        
    def removeAllValue(self, value):
        pointer = self.head
        while pointer.next != None:
            if(pointer.next.value == value):
                temp = pointer.next
                pointer.next = pointer.next.next
                temp.next = None
                self.length -= 1
            # elemen pertama
            elif self.head.value == value:
                pointer = self.head
                self.head = pointer.next
                pointer.next = None
                self.length -= 1
                return pointer.value
            else:
                pointer = pointer.next

    # elemen pertama value dihapus
    def removeValue(self, value):
        pointer = self.head
        stop = False
        while stop == False:
            if pointer.next.value == value:
                temp = pointer.next
                pointer.next = pointer.next.next
                temp.next = None
                self.length -= 1
                stop = True
                return pointer.value
            else:
                pointer = pointer.next

    # kembalikan index dari elemen pertama yang valuenya adalah value
    def findIndex(self, value):
        pointer = self.head
        stop = False
        idx = 0
        while stop == False:
            if pointer.value == value:
                stop = True
            else:
                pointer = pointer.next
                idx += 1
        return idx
    
    # kembalikan index dari elemen pertama yang memenuhi syarat yang diberikan
    def findIndexWhere(self, condition):
        pointer = self.head
        stop = False
        idx = 0
        while stop == False:
            if condition(pointer.value) == True:
                stop = True
                # print(condition(pointer.value))
                # print(idx)
            else:
                pointer = pointer.next
                idx += 1
        return idx

    # Kembalikan index dari elemen terakhir yang memenuhi syarat (condition) yang diberikan
    # Kalau tidak ketemu, kembalikan None
    def lastIndexWhere(self, condition):
        pointer = self.head
        idx = 0
        temp = None
        while pointer != None:
            if condition(pointer.value) == True:
                temp = idx
                idx += 1
                # print(temp)
            else:
                idx+=1
            pointer = pointer.next

        return temp


    # Mengembalikan List baru yang anggotanya adalah value-value yang memenuhi syarat
    # Kalau tidak ada yang memenuhi syarat, kembaliannya adalah list kosong (head == None)
    def where(self, condition):
        pointer = self.head
        temp = List()
        while pointer != None:
            if condition(pointer.value) == True:
                temp.addLast(pointer.value)
                pointer = pointer.next
            else:
                pointer = pointer.next
        return temp

    # def insert(self, index, list):
    # Menambahkan/menyisipkan list ke dalam index yang ke-index
    def insert(self, index, list):

        if index >= 1 and index <= self.length:
            pointer = self.head
            for i in range (0,index-1,1):
                pointer = pointer.next
            temp = pointer.next
            pointer.next = list.head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = temp
        elif index == 0:
            pointer = self.head # buat list lama
            self.head = list.head # head pindah ke list baru
            pointer2 = self.head
            while pointer2.next != None:
                pointer2 = pointer2.next
            pointer2.next = pointer

    def removeWhere (self, condition):
    # Menghapus semua elemen yang memenuhi syarat condition
        pointer = self.head
        temp = List()
        while pointer != None:
            if condition(pointer.value) == False:
                pass
            else:
                temp.addLast(pointer.value)
            pointer = pointer.next
        return temp


    def map(self, mapFunction):
    # Mengembalikan List baru dg elemen yang merupakan hasil mapping elemen list lama dg mapFunction
        pointer = self.head
        temp = List()
        while pointer != None:
            temp.addLast(mapFunction(pointer.value))
            pointer = pointer.next
        return temp

    def subList(self, start, end= None):
    # Mengembalikan List baru yg merupakan bagian dari list lama mulai dr index ke start hingga index ke end
    # Jika end = None atau end >= length - 1 artinya sampai akhir
    # Jika start <= 0 artinya dari awal
        pointer = self.head
        temp = List()
        index = 0
        while pointer != None:
            # print("index",index)
            # print("value",pointer.value)
            if index >= start and index <= end:
                temp.addLast(pointer.value)
            pointer = pointer.next
            index += 1
        return temp

class ListElement:
    # value adalah integer (untuk menyimpan nilai dari element ini)
    # next adalah ListElement (untuk menunjuk elemen berikutnya)
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        result = ""
        pointer = self.head

        while pointer != None: # supaya berhenti di None
            result = result + str(pointer.value) + " "
            pointer = pointer.next
        return result

    def push(self, value):
    # untuk menambahkan element yang nilainya value ke dalam stack (tumpukan plg atas)
        e = ListElement(value)
        if self.head == None:
            self.head = e
        else:
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = e
        self.length += 1

    def pop(self):
    # untuk menghapus element paling atas dari stack dan mengembalikan nilainya
        if self.length > 1 :
            pointer = self.head
            while pointer.next.next != None:
                pointer = pointer.next
            value = pointer.next.value
            pointer.next = None
        elif self.length == 1:
            value = self.head.value
            self.head = None
        else:
            value = None
        self.length -= 1 
        return value

class StackElement:
    def __init__(self,  value, next = None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        result = ""
        pointer = self.head

        while pointer != None: # supaya berhenti di None
            result = result + str(pointer.value) + " "
            pointer = pointer.next
            self.length+=1
        return result

    def enqueue(self,value):
    # untuk menambahkan elemen yg nilainya value ke dalam stack (tumpukan paling atas)
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


    def pop(self):
        pointer = self.head
        self.head = pointer.next
        pointer.next = None
        self.length -= 1
        return pointer.value

class QueueElement:
    def __init__(self,  value, next = None):
        self.value = value
        self.next = next

class QueuePriority:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        result = ""
        pointer = self.head

        while pointer != None: # supaya berhenti di None
            result = result + str(pointer.value) + " "
            pointer = pointer.next
            self.length+=1
        return result

    def enqueue(self,value,priority):
    # untuk menambahkan elemen yg nilainya value ke dalam stack (tumpukan paling atas)
        e = QueueElementPriority(value, priority)
        pointer = self.head

        if self.head == None:
            self.head = e
        else:
            pointer = self.head
            while pointer.next!= None and pointer.next.priority <= priority:
                    pointer = pointer.next
            temp = pointer.next
            pointer.next = e
            pointer.next.next = temp
        self.length += 1


    def pop(self):
        pointer = self.head
        self.head = pointer.next
        pointer.next = None
        self.length -= 1
        return pointer.value

class QueueElementPriority:
    def __init__(self,  value, priority, next = None):
        self.value = value
        self.priority = priority
        self.next = next


# fungsi mencari value > 10
def syarat(value):
    if value > 10:
        return True
    else:
        return False

# map function value = value * -1
def mapFunction(value):
    value = value * -1
    return value

def factorial(value):
# 0! = 1
# 1! = 1
# 2! = 2 x 1
# 3! = 3 x 2 x 1
    if value+1 == 0: return 1
    f = 1
    for i in range(2,value+1):
        f = f * i
    return f


def main():
    # x = List()
    # e5 = ListElement(5)
    # e4 = ListElement(4, next= e5)
    # e3 = ListElement(3, next= e4)
    # e2 = ListElement(2, next= e3)
    # e1 = ListElement(1, next= e2)
    # x.head = e1

    # x = Stack()
    # e5 = StackElement(5)
    # e4 = StackElement(4, next= e5)
    # e3 = StackElement(3, next= e4)
    # e2 = StackElement(2, next= e3)
    # e1 = StackElement(1, next= e2)
    # x.head = e1
    # x.push(1)
    # x.push(2)
    # x.push(3)
    
    # x = Queue()
    # e5 = QueueElement(5)
    # e4 = QueueElement(4, next= e5)
    # e3 = QueueElement(3, next= e4)
    # e2 = QueueElement(2, next= e3)
    # e1 = QueueElement(1, next= e2)
    # x.head = e1
    # print(x)
    # print(x.length)
    # x.enqueue(10)
    # x.enqueue(11)
    # print(x)
    # x.pop()
    # print(x)

    # print(x)
    # print(x.length)
    # print(x.pop())
    # print(x)
    # print(x.length)

    # x = QueuePriority()
    # x.enqueue(10,1)
    # x.enqueue(11,1)
    # x.enqueue(9,2)
    # print("10 11 9: ",x)
    # x.enqueue(8,2)
    # print("10 11 9 8: ",x)
    # x.enqueue(9,1)
    # print("10 11 9 9 8: ",x)
    # x.enqueue(100,2)
    # print("10 11 9 9 8 100: ",x)
    # x.pop()
    # print("11 9 9 8 100: ",x)

    print(factorial(4))

    # x.addLast(1)
    # x.addLast(21)
    # x.addLast(11)
    # x.addLast(10)
    # x.addLast(2)
    # x.addLast(12)
    # x.addLast(34)
    # x.addFirst(5)
    # x.insertData(44,6)
    # print(x)
    # print(x.length)
    # x.removeFirst()
    # x.removeLast()
    # x.removeIndex(10)
    # x.removeAllValue(20)
    # x.removeValue(21)
    # print(x.findIndex(21))
    # print(x.findIndexWhere(syarat))
    # print(x.lastIndexWhere(syarat))
    # print(x.where(syarat))
    # listHasilWhere = x.where(syarat)
    # x.insert(0, listHasilWhere)
    # print(x)
    # print(x.removeWhere(syarat))
    # print(x.map(mapFunction))
    # print(x.subList(-1,6))

main()
