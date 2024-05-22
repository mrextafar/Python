class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

    def display(self):
        current = self.head
        for i in range(self.length+1):
            if i == self.length:
                print(f"Объект - {current.data}, ссылка - Нет")
            else:
                print(f"Объект - {current.data}, ссылка - {current.next.data}")
            current = current.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        self.length += 1

    def remove(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.length -= 1
                return
            current = current.next

    def insert(self, index, data):
        if index < 0 or index > self.length:
            raise IndexError("Индекс вне диапазона списка.")

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.length += 1
