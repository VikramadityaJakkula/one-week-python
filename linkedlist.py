from exceptions import Empty

class linkedlist:

    class node:
        __slots__ = '_element','_next'
        
        def  __init__(self,element,next):
            self._element = element
            self._next = next
        
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
        
    def is_Empty(self):
        if (self.size == 0):
            print ("Is empty")
        else:
            print(self.size)
    
    def add_first(self,ele):
        newest = self.node(ele,None)
        if (self.size == 0 ):
            self.head = newest
            self.tail = newest
        else:
            newest.tail = self.head
            self.head = newest
            self.size = self.size + 1
    
    def add_last(self,ele):
        newest = self.node(ele,None)
        if (self.size == 0 ):
            self.head = newest
            self.tail = newest
        else:
            self.tail._next = newest
        self.tail = newest
        self.size += 1

    def add_any(self,ele,position):
        newest = self.node(ele,None)
        loc = self.head
        i = 0
        if (self.size == 0 ):
            self.head = newest
            self.tail = newest
        else:
            while (i < position):
                i += 1
                loc = loc._next
            newest.head = loc._next
            loc.next = newest
            size += 1
    
    def remove_first(self):
        if self.is_Empty():
            raise Empty('lINKED lIST EMPTY')
        value = self.head._element
        self.head = self.head._next
        size -= 1
        if self.is_Empty() == 0:
            self.tail = None
        return value
    
    def remove_last(self):
        if self.is_Empty():
            raise Empty('lINKED lIST EMPTY')
        i = 0
        loc = self.head
        while (i< len(self) - 2):
            i += 1
            loc = loc._next
        value = loc._next._element
        self.tail = loc
        loc = loc._next
        self.tail._next = None
        self.size -=1
        return value
    
    def remove_any(self,position):
        if self.is_Empty():
            raise ('lINKED lIST EMPTY')
        i = 0
        loc = self.head
        while(i<position-1):
            i+= 1
            loc = loc._next
        value = loc._next._element
        loc._next = loc._next._next
        size -= 1
        return value
    
    def display(self):
        location = self.head
        while location:
            print (location._element,end = "-->")
            location = location._next
        print ()


L = linkedlist()
L.add_last(10)
L.add_last(20)
L.add_last(30)
L.display()
L.remove_last()
L.display()

















