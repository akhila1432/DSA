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

    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
           return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
           if itr.data == data_after:
              itr.next = Node(data_to_insert,itr.next)
              break
           itr = itr.next
    
    def remove_by_value(self, data):

        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


                 

ll = Linkedlist()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple")
ll.print()
ll.remove_by_value("orange")
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()

    
        
