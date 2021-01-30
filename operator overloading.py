#operator overloading

class point:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return f"({self.a},{self.b})"
    def __add__(self,obj2):
        a = self.a + obj2.a
        b = self.b + obj2.b
        return point(a,b)
        
p1 = point(2,4)
p2 = point(5,10)

print(p1+p2)
print(p1)
