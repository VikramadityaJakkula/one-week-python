import exceptions

class stackarray:
    def __init__(self):
        self.data = []

    def __len(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data) == 0
    
    def pop(self,e):
        if self.is_empty():
            raise exceptions.Empty()
        else:
            self.data.pop()
             
    def push(self,e):
        self.data.append(e)
    
    def top(self):
        if self.is_empty():
            raise exceptions.Empty()
        else:
            print(self.data[-1])


A = stackarray()

A.push(10)
A.push(20)
A.push(30)

print(A.data)

A.top()

A.pop(10)

print(A.data)

