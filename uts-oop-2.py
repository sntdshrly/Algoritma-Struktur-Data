# 2072025 Sherly Santiadi

class ListElement:
    # value: int (untuk menyimapn nilai)
    # next: ListElement (untuk menunjuk pada element berikutnya)
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class List:
    head = None  # untuk menunjuk element pertama dari List

    def addFirst(self, value):
        if self.head == None:
            self.head = ListElement(value=value)
        else:
            new_element = ListElement(value=value, next=self.head)
            self.head = new_element

    def __str__(self):
        result = ""
        pointer = self.head
        while pointer != None:
            result = result + str(pointer.value) + " "
            pointer = pointer.next
        return result

    # def count(self):
    def count(self):
        counter = 0
        pointer = self.head
        while pointer != None:
            counter = counter + 1
            pointer = pointer.next
        return counter

    # def indexOf(self, value):
    def indexOf(self, valueOfList):
        index = -1
        value = None
        pointer = self.head
        while pointer != None and value == None:
            index = index + 1
            if pointer.value == valueOfList:
                value = index

            pointer = pointer.next
        return value


def main():
    list = List()

    list.addFirst(4)
    list.addFirst(1)
    list.addFirst(6)
    list.addFirst(4)
    list.addFirst(8)
    list.addFirst(1)
    list.addFirst(2)
    list.addFirst(9)

    print(list)
    print("Jumlah element list:", list.count())
    print("Index dari elemen yang bernilai 9:",
          list.indexOf(9))  # index dimulai dari 0
    print(
        "Index dari elemen yang bernilai 1:", list.indexOf(1)
    )  # index yang dikembalikan adalah index yang paling pertama
    print(
        "Index dari elemen yang bernilai 100:", list.indexOf(100)
    )  # mengembalikan None jika List tidak memiliiki nilai yang dicari


main()
