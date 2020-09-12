"""A Doubly Linked List (DLL) contains an extra pointer, 
typically called previous pointer, 
together with next pointer and data which are there in singly linked list."""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_size = 0

    def add_first(self, value):
        node = Node(value)
        if self.head == None:
            self.head = self.tail = node
        elif self.head == self.tail:
            node.next = self.head 
            self.head.prev = node
            self.head = node
            self.tail = node.next
        else:
            node.next = self.head 
            self.head.prev = node
            self.head = node
        self.current_size += 1
        return 

    def add_last(self, value):
        node = Node(value)
        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail 
            self.tail = node
        self.current_size += 1
        return 

    def remove_first(self):
        data = None
        if self.head == None:
            return None
        elif self.head == self.tail:
            data = self.head.data
            self.head = self.tail = None
        else:
            data = self.head.data
            self.head.next.prev = None
            self.head = self.head.next
        self.current_size -= 1
        return data

    def remove_last(self):
        data = None
        if self.tail == None:
            return None
        elif self.head == self.tail:
            return self.remove_first()
        else:
            data = self.tail.data
            self.tail.prev.next = None
            self.tail = self.tail.prev
        self.current_size -= 1
        return data

    def remove(self, value):
        current = self.head
        while current != None:
            if current.data == value:
                if self.head == current:
                    return self.remove_first()
                elif self.tail == current:
                    return self.remove_last()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.current_size -= 1
                    return current.data
            current = current.next 
        return None

    def find(self, value):
        current = self.head
        while current != None:
            if current.data == value:
                return True
            current = current.next
        return False

    def peak_first(self):
        if self.head == None:
            return None
        return self.head.data

    def peak_last(self):
        if self.tail == None:
            return None
        return self.tail.data
    
    def print(self):
        current = self.head
        while current != None:
            print(current.data, end=', ')
            current = current.next
        print()


dll = DoubleLinkedList()

dll.add_first(10)
dll.add_first(9)
dll.add_last(12)
dll.add_last(13)
dll.add_first(1)
dll.print()
print(dll.remove_first())
dll.print()
print(dll.remove_last())
dll.print()
print(dll.find(13))
print(dll.find(10))
print(dll.remove(10))
dll.print()