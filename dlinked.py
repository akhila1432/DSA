class node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        Node = node(data, self.head)
        self.head = Node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '--->'
            itr = itr.next
        print(listr)

ll=linkedlist()
ll.insert_at_begining(5)
ll.insert_at_begining(89)
ll.print()