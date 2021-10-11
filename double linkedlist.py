class Node:

    def __init__(self, data=None, next = None, prev = None,):

        self.prev = prev
        self.data = data
        self.next = next

    def double_linkedlist(self):
        self.head = None

    def insert_at_begining(self,data):
        if self.head is None:
           new_node = Node(data,self.head,None)
           self.head = new_node
        else:
            new_node = Node(data,self.head,None)
            self.head.prev = new_node
            self.head = new_node
   
    def insert_at_end(self,data):
        
        if self.head is None:
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None, itr)
    
    def inser_at(self,data):

        if self.head is None:
            return

        if self.head == data:
            self.head.next = None
            



        