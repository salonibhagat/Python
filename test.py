class A:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

class B(A):
    def add(self):
        return self.num1 + self.num2 
    
    def sub(self):
        return self.num1 - self.num2 
class C(B):
    def display(self):
        print("Addition of two number is: ", self.add())
        print("Difference between two number is: ", self.sub())



O1 = C(50,20)
O1.display()
print(O1.add())

