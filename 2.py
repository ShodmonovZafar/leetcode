class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self, val):
        self.data = val

    def setNext(self, val):
        self.next = val

  
class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head is None

    def add(self, item):
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node
    
