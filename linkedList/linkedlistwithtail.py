#adding a tail pointer to the end of the linked list will give us o(1) when getting the last item in linkedlist

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linkedlist:
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
            self.tail = node.next
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.current_size += 1
        return
    def add_last(self, value):
        node  = Node(value)

        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
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
            self.head = self.head.next
        self.current_size -= 1
        return data
    
    def remove_last(self):
        data = None
        if self.head == None:
            return None
        elif self.head == self.tail:
            return self.remove_first()
        else:
            data =  self.tail.data
            prev = None
            current = self.head
            while current != self.tail:
                prev = current 
                current = current.next
            prev.next = None
            self.tail = prev
        self.current_size -= 1
        return data

    def remove(self, value):       
        current = self.head
        prev = None
        while current != None:
            if current.data == value:
                if self.head == current:
                    return self.remove_first()
                elif self.tail == current:
                    return self.remove_last()
                else:
                    prev.next = current.next
                    self.current_size -= 1
                    return current.data
            prev = current 
            current = current.next
        
        return None 

    def find(self, value):
        current = self.head
        while current != None:
            if current.data == value:
                return True 
            current = current.next
        
        return False

    def peek_first(self):
        if self.head == None:
            return None
        return self.head.data

    def peek_last(self):
        if self.tail == None:
            return None
        return self.tail.data

    def print(self):
        current  = self.head
        while current:
            print(current.data, end=", ")
            current = current.next
        print()
ll = Linkedlist()

ll.add_first(10)
ll.add_first(9)
ll.add_last(12)
ll.add_last(13)
ll.add_first(1)
ll.print()
print(ll.remove_first())
ll.print()
print(ll.remove_last())
ll.print()
print(ll.find(13))
print(ll.find(10))
print(ll.remove(10))
ll.print()