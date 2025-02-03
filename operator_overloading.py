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