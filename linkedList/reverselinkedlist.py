

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = Node(head)

    def add(self,val):
        node = Node(val)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node                
        else:
            self.head = node

    def showNodesList(self):
        nodes = []
        if self.head:
            current = self.head
            while current:
                nodes.append(current.val)
                current = current.next
        return nodes
        
    def reverse(self):
        self.head = self.reverseLinkedList(self.head)


    def reverseLinkedList(self,head):
        '''Reverses a linked list using 3 pointers previous, current, and following. 
        We want to look at every node and reassign its next property to what ever came before it (previous) while not losing track of what comes after current (following)'''
        previous = None 
        current = head
        following = head

        while current != None:
            following = following.next
            current.next = previous 
            previous =  current 
            current = following 


        return previous #since the while loop is running until current is null we return previous which is pointing to the node before current




myLinkedList = LinkedList(1)

myLinkedList.add(2)
myLinkedList.add(3)
myLinkedList.add(4)
myLinkedList.add(5)

print(myLinkedList.showNodesList())
myLinkedList.reverse()
print(myLinkedList.showNodesList())
