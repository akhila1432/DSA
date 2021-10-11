class Node:

    def __init__(self,data =None, next = None):
        self.data=data
        self.next=next
    
class Linkedlist:

    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def print(self):
        if self.head is None:
            print('Linkedlist is empty')
            return
       
        itr = self.head
        llsr = ''
        while itr:
            llsr += str(itr.data) + '-->'
            itr = itr.next
        print(llsr)

ll=Linkedlist()
ll.insert_values(["banana",'eggs','mango','breaad','fish'])
ll.print()

    
        
