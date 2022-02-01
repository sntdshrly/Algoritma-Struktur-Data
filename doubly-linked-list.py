from multiprocessing.sharedctypes import Value


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

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

    def addLast(self, value):
        e = ListElement(value)
        if self.head == None:
            e.next = None
            e.prev = None
            self.head = e
            self.tail = e
        else:
            self.tail.next = e
            e.prev = self.tail
            self.tail = e

        self.length += 1

    def addFirst(self, value):
        e = ListElement(value)

        self.head.prev = e
        e.next = self.head
        self.head = e
        self.length += 1

    def insertData(self, value, index):

        pointer = self.head

        if index <= 0:
            self.addFirst(value)
        elif index >= self.length:
            self.addLast(value)
        else:
            prevIndex = index - 1
            pointer = self.head
            currentIndex = 0

            while currentIndex != prevIndex:
                pointer = pointer.next
                currentIndex = currentIndex + 1

                newElement = ListElement(value)
                pointer.next.prev = newElement
                newElement.next = pointer.next
                newElement.prev = pointer
                pointer.next = newElement

        self.length += 1

    def removeFirst(self):
        pointer = self.head

        self.head = pointer.next
        self.head.prev = None
        pointer.next = None
        self.length -= 1
        return pointer.value

    def removeLast(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def removeIndex(self, index):
        pointer = self.head
        if index <= 0:
            return self.removeFirst()
        elif index >= self.length-1:
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
            self.length -= 1
            return temp.value

    def removeAllValue(self, value):
        if self.length > 0:

            if self.head.value == value:
                self.head = self.head.next
                self.head.prev = None
                self.length -= 1

            if self.tail.value == value:
                self.tail = self.tail.prev
                self.tail.next = None

            pointer = self.head
            while pointer.next != None:  # cek sampe element terakhir
                if pointer.next.value == value:  # elemen awal dilewat dulu
                    pointer.next.next.prev = pointer
                    pointer.next = pointer.next.next

                    self.length -= 1

                pointer = pointer.next

    def removeValue(self, value):
        if self.head.value == value:
            return self.removeFirst()

        if self.length > 1:
            pointer = self.head
            cek = 1
            while cek != 0:
                if pointer.next.value == value:
                    temp = pointer.next
                    pointer.next = temp.next
                    pointer.next.next.prev = pointer

                    temp.next = None
                    temp.prev = None
                    self.length -= 1
                    cek == 0
                    return
                else:
                    pointer = pointer.next


class ListElement:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def main():
    x = List()

    x.addLast(1)
    x.addLast(2)
    x.addLast(3)
    x.addLast(4)
    x.addLast(5)
    x.addLast(4)
    # x.addFirst(100)
    # x.insertData(999, 2)
    # x.removeFirst()
    # x.removeLast()
    # x.removeIndex(3)
    # x.removeAllValue(1)
    x.removeValue(4)

    print("print backward: ")
    x.printBackward()
    print()
    print("-"*30)
    print("print forward: ")
    x.printForward()


main()
