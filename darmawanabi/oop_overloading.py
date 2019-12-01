class A:
    
    def __init__(self, a):
        self.a = a
    
    def add(self, b):
        return self.a + b.a
    

obj1 = A(1)
obj2 = A(2)
obj3 = A("hemmmm")
obj4 = A("apasii")

print(obj1 + obj2)
print(obj3 + obj4)

# masih error
