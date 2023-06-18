class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def prepend(self, value):
        node = Node(value)
        self.length += 1

        if (self.head == None):
            self.head = node
            self.tail = node
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = node

    def append(self, value):
        node = Node(value)
        self.length += 1

        if (self.tail == None):
            self.tail = node
            self.head = node
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def insertAt(self, idx, value):
        if (
            idx < 0 or
            idx > self.length
        ):
            return
        elif (idx == 0):
            return self.prepend(value)
        elif (idx == self.length):
            return self.append(value)
        
        curr = self.head
        i = 0
        while (i < idx - 1):
            curr = curr.next
            i += 1
        
        node = Node(value)
        self.length += 1
        node.prev = curr
        node.next = curr.next
        curr.next = node
        node.next.prev = node
    
    def get(self, idx):
        if (
            self.length == 0 or
            idx < 0 or
            idx >= self.length
        ):
            return None
        
        curr = self.head
        i = 0
        while (curr != None):
            if (i == idx):
                return curr.value
            curr = curr.next
            i += 1
    
    def removeAt(self, idx):
        if (
            self.length == 0 or
            idx < 0 or
            idx >= self.length
        ):
            return None

        if (idx == self.length - 1):
            node = self.tail
            self.length -= 1

            if (self.length == 0):
                self.tail = None
                self.head = None
                node.next = None
                node.prev = None
                return node.value
            
            self.tail = self.tail.prev
            node.next = None
            node.prev = None
            return node.value
        
        if (idx == 0):
            node = self.head
            self.length -= 1

            if (self.length == 0):
                self.head = None
                self.tail = None
                node.next = None
                node.prev = None
                return node.value

            self.head = self.head.next
            node.next = None
            node.prev = None
            return node.value

        curr = self.head
        i = 0
        while (i < idx):
            curr = curr.next
            i += 1
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.length -= 1

        curr.next = None
        curr.prev = None
        return curr.value
    
    def remove(self, value):
        if (self.head == None):
            return None

        curr = self.head
        i = 0
        while (curr != None):
            if (curr.value == value):
                return self.removeAt(i)
            
            curr = curr.next
            i += 1

        return None

    def print(self):
        if (self.length == 0):
            return
        
        curr = self.head
        while (curr != None):
            print(curr.value)
            curr = curr.next