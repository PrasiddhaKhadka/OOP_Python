class Number:
    a = 10
    b = 20
    
    def __init__(self,n):
        self.n = n
        
    def __add__(self,other):
        return self.n + other.n
    
    def __floordiv__(self,num):
        return self.n // num.n
        

n = Number(30)
m = Number(40)        

print(n + m)
print(n // m)



class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def __add__(self,other):
        return Complex(self.real + other.real, self.img + other.img)
    
    def __mul__(self,other):
        return Complex(self.real * other.real, self.img * other.img)
    
    
    def __str__(self):
        return f"{self.real} + {self.img}i"
    
    
    
    
c1 = Complex(10,20)
c2 = Complex(30,40) 
print(c1 + c2)  
print(c1 * c2)