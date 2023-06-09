class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def prepend(self, value):
        self.length += 1
        node = Node(value)

        node.next = self.head
        self.head = node
    
    def append(self, value):
        self.length += 1
        node = Node(value)

        if (self.head == None):
            self.head = node
            return

        curr = self.head
        while (curr.next != None):
            curr = curr.next
        curr.next = node
    
    def insertAt(self, idx, value):
        if (idx < 0 or idx > self.length):
            raise Exception("Cannot insert at " + str(idx))
        elif (idx == self.length):
            return self.append(value)
        elif(idx == 0):
            return self.prepend(value)
        
        curr = self.head
        i = 0
        while True:
            if (i == (idx - 1)):
                break

            curr = curr.next
            i += 1
        
        self.length += 1
        node = Node(value)
        node.next = curr.next
        curr.next = node
    
    def get(self, idx):
        if (self.head == None):
            return None

        if (idx < 0 or idx >= self.length):
            return None

        curr = self.head
        i = 0
        while True:
            if (i == idx):
                break

            curr = curr.next
            i += 1
        
        return curr.value

    def removeAt(self, idx):
        if (
            self.head == None or
            idx < 0 or
            idx >= self.length
        ):
            return None
        
        if (idx == 0):
            node = self.head
            self.length -= 1

            self.head = self.head.next
            node.next = None
            return node.value
        
        curr = self.head
        i = 0
        while True:
            if (i == (idx - 1)):
                break

            curr = curr.next
            i += 1
        
        node = curr.next
        curr.next = curr.next.next
        node.next = None
        return node.value
    
    def remove(self, value):
        if (self.head == None):
            return None
        
        curr = self.head
        i = 0
        while (curr.next):
            if (curr.value == value):
                return self.removeAt(i)

            curr = curr.next
            i += 1
        
        return None