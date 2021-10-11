class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        new_node = Node(data,self.head)
        self.head = new_node

    def print(self):
        if    self.head is None:
            print('Linkedlist is empty')

           