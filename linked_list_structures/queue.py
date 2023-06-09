class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def enqueue(self, value):
        self.length += 1
        node = Node(value)
        node.next = None

        if (self.tail == None):
            self.tail = node
            self.head = node
            return
        
        self.tail.next = node
        self.tail = node
    
    def dequeue(self):
        if (self.head == None):
            return None
        
        self.length -= 1
        ret = self.head
        self.head = self.head.next

        if (self.head == None):
            self.tail = None
        
        ret.next = None
        return ret.value
    
    def peek(self):
        if (self.head == None):
            return None
        
        return self.head.value