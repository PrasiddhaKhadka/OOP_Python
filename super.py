class Employee:
    a = 10
    
    def __init__(self) -> None:
        print("this is constructor of employee")
        
        

class Programmer(Employee):
    b = 20
    
    def __init__(self) -> None:
        print("this is constructor of Programmer")

class Manager(Programmer):
    c = 30
    def __init__(self) -> None:
        super().__init__()
        print("this is constructor of Manager")
    

# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.a)
# print(o.b)

o = Manager()
print(o.a)
print(o.b)
print(o.c)
