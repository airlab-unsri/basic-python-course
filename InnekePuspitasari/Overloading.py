class K:
    def __init__(self, k):
        self.k = k

    # adding two objects
    def __add__(self, o):
        return self.k + o.k
ob1 = K(1)
ob2 = K(2)
ob3 = K("Geeks")
ob4 = K("For")

print(ob1 + ob2)
print(ob3 + ob4)