import Node
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail=None

    def prepend(self, data):
        new_node = Node.Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) + " -> None"
    
    def is_empty(self):
        if not self.head:
            return True
        return False
    
    def append(self, data):
        new_node = Node.Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def append_tail(self, data):
        node = Node.Node(data)
        if self.tail is None:  # lista vacía
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def pop_first(self):
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        return value
    
    
    def pop(self):  # eliminar cola
        if self.is_empty():
            raise IndexError("lista vacía")
        if self._size == 1:
            return self.pop_first()
        prev = self._node_at(self._size - 2)
        data = prev.next.data
        prev.next = None
        self.tail = prev
        self._size -= 1
        return data


sll = SinglyLinkedList()
sll.prepend(5)
sll.prepend(10)
sll.prepend(15)
sll.prepend(20)
sll.prepend(25)
sll.append(3)
sll.append(4)

sll.pop_first()
print(sll)
