class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self,other):
        return Complex((self.a + other.a), (self.b + other.b))
    
    def __sub__(self,other):
        return Complex((self.a - other.a), (self.b - other.b))
    
    def __mul__(self, other):
        return Complex((self.a * other.a) + (self.b*other.b*-1), (self.a*other.b) +(self.b*other.a))
    
    def __repr__(self):
        return f"{self.a} + {self.b}i"
    
    def __iadd__(self,other):
        self.a += other.a
        self.b += other.b




cplx1 = Complex(5, 2)
print(cplx1)


cplx2 = Complex(3, 3)
print(cplx2) #3 + 3i

#addition
print(cplx1 + cplx2) #8 + 5i

#subtraction
print(cplx1 - cplx2) #2 - 1i

#multiplication First Outer Inner Last


print(cplx1 * cplx2) #9 + 21i
#original objects remain unchanged
print(cplx1) #5 + 2i
print(cplx2) #3 + 3i