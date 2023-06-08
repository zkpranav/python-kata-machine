class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
    
class Stack:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def push(self, value):
        node = Node(value)
        node.prev = self.head
        self.head = node
        self.length += 1
    
    def pop(self):
        if (self.head == None):
            return None
        
        self.length -= 1
        node = self.head
        self.head = self.head.prev
        node.prev = None

        return node.value

    def peek(self):
        if (self.head == None):
            return None
        
        return self.head.value
