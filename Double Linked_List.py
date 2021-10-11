#................................... Create a Class Node ........................

class Node:

#..................................Initialize the method for the variables .........................

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

#..................................... Create a Class Double Linkedlist ...................

class doublelinkedlist:
         

#....................................... Initialize the method for head .....................

    def __init__(self):
        self.head = None


#.......................................... do the forward traversal define a function .................

    def forward_traversal(self):
        if self.head is None:
           print('Linked list is empty')
        else:
           n =  self.head
           while n is not None:
                 print(str(n.data) + '--->',end='')
                 n = n.next

#......................................... do the backward traversal for that define a function ...........................
 
   
    def backward_traversal(self):
        print()
        if self.head is None:
           print('Linked list is empty')
        else:
            n = self.head
            while n.next is not None:
                  n = n.next
            while n is not None:
                  print(str(n.data) + '--->',end='')
                  n = n.prev


#......................................... insert first element when the linkedlist is completely empty .................................

    def insert_empty(self,data):
        if self.head is None:
           new_node = Node(data)
           self.head = new_node
        else:
           print('Linked list is empty')


#....................................... define a method to insert a element in the first ................

    def insert_at_first(self,data):
        if self.head is None:
           new_node = Node(data)
           self.head = new_node
        else:
           new_node = Node(data)
           new_node.next = self.head
           self.head.prev = new_node
           self.head = new_node


#....................................... define method insert the element at the end ..............................

    def insert_at_end(self,data):
        if self.head is None:
           new_node = Node(data)
           self.head = new_node
        else:
           n = self.head
           while n.next is not None:
                 n = n.next
           new_node = Node(data)
           n.next = new_node
           new_node.prev = n


#........................................... Create a Method Called print to show the outputs ......................................

    def print(self):
        if self.head is None:
            print('Linkedlist is empty')
            return
       
        n = self.head
        llsr = ''
        while n:
            llsr += str(n.data) + '-->'
            n = n.next
        print(llsr)

#..................... Create a Object for the doubblelinkedlist ....................................................

dl = doublelinkedlist()
dl.forward_traversal()
dl.backward_traversal()
dl.insert_empty(10)
dl.print()
dl.insert_at_first(11)          
dl.print()
dl.insert_at_end(9)           
dl.print()             
dl.forward_traversal()
dl.backward_traversal()