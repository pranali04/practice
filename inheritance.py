# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#print("Hello world")
class math:
    def __init__(self,a,b):
        print("math class")
class divide(math):
    def __init__(self,a,b):
        self.a = a
        self.c = b
        print("divide initialized")
        #super().__init__(a,b)
    def divide(self):
        print(self.a/self.c)

class mult(math):
    def __init__(self,a,b):
        #divide.__init__(self,b,c)
        print("mult function ini")
        #super().__init__(a,b)
        self.a = a
        self.b = b
      
    def divide(self):
        print("overrrrrr")
    #def divide(self,a,b):
        #print("from mult class")
        #print(a/b)
    
    def mult(self):
        print(self.a*1)

class calc(mult,divide):
    def __init__(self,a,b):
        super().__init__(a,b)
    def printing(self):
        super().divide()
#def common_int(obj):
#    obj.divide()

A = calc(4,6)
del A.a
print(A.b)
#B = mult(6,8)
#common_int(A)
#common_int(B)

A.printing()
#print(calc.__mro__)
#A.divide()
#A.divide(2,8)
#A.mult()
    
