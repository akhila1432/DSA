#..................... define a class of Node ...........

class Node:
#..................... definie the initialization of the node ......................


    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


#................... creating a class called Linkedlist ..............................


class Linkedlist:
    def __init__(self):
        self.head = None



#.................... Insertion at the begining of the linkedlist ..................
   
    def insert_at_first(self,data):
       new_node = Node(data,self.head)
       self.head = new_node

#..................... Insertion at the end of the linkedlist ..................



    def insert_at_last(self,data):
        if self.head is None:
           self.head = Node(data, None)
           return
        itr = self.head
        while itr.next:
              itr = itr.next

        itr.next = Node(data,None)

#............................ get the length of the linked list so it would be easy to insert at what position ...................



    def get_length(self):
        if self.head is None:
           return
        itr = self.head
        count = 0
        while itr:
              count+=1
              itr = itr.next
        

             
#........................ Insertion at the position ..............................

 

    def insert_at(self,index,data):
         if index < 0 or index > self.get_length():
            raise Exception('Invalid index')

         if index == 0:
            self.insert_at_first(data)
            return
 
         count = 0
         itr = self.head
         while itr:
            if count == index -1:
               new_node = Node(data,itr.next)
               itr.next = new_node
               break
            itr = itr.next
            count+=1
            

#............................. delete an element from first .............................


    def delete_at_first(self):
         if self.head is None:
            return
         itr = self.head
         while itr:
               itr.next = self.head
         itr = itr.next
         

#.............................. delete an element from last ..........................


    def delete_at_last(self):
        if self.head is None:
           print('Linked list is empty')
        itr = self.head
        while itr.next.next is not None:
              itr = itr.next
        itr.next = None


#........................... delete an element in between with the index ..................................


    def delete_at(self,index):
       if self.head is None:
          print('Linked list is empty')
       if index<0 or index>self.get_length():
          raise Exception ('invalid index')
       if index == 0:
          self.head = self.head.next
     
       count = 0
       itr = self.head
       while itr:
            if count == index-1:
               itr.next = itr.next.next
               break
       itr = itr.next
       count+=1

#........................... insert by values such as list,tuples,etc, ....................................


    def insert_by_value(self,data_value):
       if self.head is None:
          for data in data_value:
              self.insert_at_last(data)

#............................ insert value after value ....................................................

    def insert_after_value(self, data_after, data_to_insert):
       if self.head is None:
          return
       if self.head.data == data_after:
          self.head.next = Node(data_to_insert , self.head.next)
          return
       itr = self.head
       while itr:
            itr.data == data_after
            itr.next = Node(data_to_insert, itr.next)
            break
       itr = itr.next


#.................................. remove by value .........................................................

    def remove_after(self,data):
      if self.head is None:
         return
      if self.head.data == data:
         self.head = self.head.next
      itr = self.head
      while itr:
            if itr.next.data == data:
               itr.next = itr.next.next
               break
            itr = itr.next

       

#........................ print methods that are inserted items ...........................
    def print(self):
       if Linkedlist is None:
          print('Linkedlist is empty')
      
       itr = self.head
       llr = ' '
       while itr:
            llr+= str(itr.data) + '-->'
            itr = itr.next

       print(llr) 

ll1=Linkedlist()
ll1.print()
ll1.insert_by_value(["banana","mango","grapes","orange"])
ll1.print()
ll1.insert_after_value("mango","apple")
ll1.print()
      

  


   

   