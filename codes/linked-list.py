class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def print_list(self):
        while self.head:
            print(self.head.data)
            self.head = self.head.next



linkedList = LinkedList()

linkedList.push(3)
linkedList.push(2)
linkedList.push(1)
linkedList.push(0)

print(linkedList.length) 
linkedList.print_list()