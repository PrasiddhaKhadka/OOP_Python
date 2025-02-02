import math

class Programmer:
    listProgrammer = []  
    
    def __init__(self, details):
        self.details = details  
    
    def __str__(self):
        return f"{self.details['name']} is {self.details['age']} years old from {self.details['country']}"    
    
    def add(self):
        Programmer.listProgrammer.append(self.details)  

p1 = Programmer({"name": "John", "age": 36, "country": "Norway"})       
p1.add()
p2 = Programmer({"name": "Rams", "age": 32, "country": "Norway"})       
p2.add()

print(Programmer.listProgrammer)  




class Calculator:
    
    number = 0
    
    def __init__(self, number):
        self.number = number
        
    def __str__(self):
        return f"number is {self.number}"    
    
    def calulation(self):
        Calculator.number = self.number ** 2
        print(f"Square of {self.number} is {Calculator.number}")
        
        Calculator.number = self.number ** 3
        print(f"Cube of {self.number} is {Calculator.number}")
        
        
        Calculator.number = math.sqrt(self.number)
        print(f"Square root of {self.number} is {Calculator.number}")
        
        print(Calculator.number)
        
        
        
        
cal = Calculator(4)
print(cal.calulation())        



class Demo:
    a = 4
    
o = Demo()
print(o.a)
o.a = 5
print(o.a)
print(Demo.a)