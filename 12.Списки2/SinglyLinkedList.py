class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

    def display(self):
        print(f"Lenght = {self.length}")
        current = self.head
        res = dict()
        for i in range(self.length):
            if i == self.length-1:
                res[current.data] = None
            else:
                res[current.data] = current.next.data
            current = current.next
        return res


    def append(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            self.length = 1
            return

        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode
        self.length += 1

    def removeByData(self, data):
        if self.head == None:
            print("Пустой список")
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.length -= 1
                return
            current = current.next