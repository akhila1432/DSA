class Hashtable:
    def __init__(self):
        self.max = 100
        self.arr = ([None for i in range(self.max)])

    def get_hash(self, key):
         h=0
         for char in key:
             h+= ord(char)
         return h%self.max

    def add(self,key,val):
        h= self.get_hash(key)
        self.arr[h] = val
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
    
    def get(self,key):
        h = self.get_hash(key)
        print(self.arr[h])     
t = Hashtable()
t.add('march 6',130)
print(t.arr)
t.__delitem__('march 6')
print(t.arr)
