class Car:
    #class attributes
     color = "red"
     model = "bmw"
     year = "2020"
     price = "$10000"
     is_new = True
  
#car = object 
car = Car()

# object attributes add || instance attributes add 
car.name = "Model X"

#methods
print(car.color)
print(car.model)
print(car.year)
print(car.price)
print(car.is_new)
print(car.name)  


# Advanced Classes

class Person:
    name = ""
    age = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
    def __str__(self):
        return f"{self.name} is {self.age} years old"
        
    #if not a static method then pass self    
    def add(self):
        return 5+6  
    
    #for static method
    @staticmethod  
    def mult():
        return 5*6
        
p1 = Person("John",7)

print (p1)

print(p1.add())
print(p1.mult())


# p1.add()
# -------> AFAI JANI RAHECHA <--------
#p1.add(p1)



# ----------> this keyword (Self) <----------

# 1. self keyword (this) is used to refer the current instance of the class
# 2. self keyword is used to access the attributes and methods of the class
# 3. to remove the ambiguity between the local variable and the class attribute
# 4. for default constructor
# 5.