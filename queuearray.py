from exceptions import Empty

class queuearray:

    def __int__(self):
        self.data = []
        self.size = 0
        self.front = 0

    def __len__(self):
        return len(self.size)

    def first(self):
        if self.is_empty:
            raise "Queue is empty"
        else:
            return (self.data[self.front])

    def is_empty(self):
        return (self.size == 0)

    def enqueue(self,e):
        self.data.append(e)
        self.size = self.size + 1

    def dequeue(self):
        if self.size == 0:
            raise "Queue is Empty"
        value = self.data[self.front]
        self.data[self.front] =  None
        self.size = self.size -1
        self.front = self.front + 1
        return value


c = queuearray()

print(c)

c.enqueue(10)
c.enqueue(20)
c.enqueue(30)

print(c,c.size)

print(c.dequeue())

print(c,c.size)





    