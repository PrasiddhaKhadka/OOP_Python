class Employee:
    a = 10

class Programmer(Employee):
    b = 20

class Manager(Programmer):
    c = 30
    

o = Employee()
print(o.a)

o = Programmer()
print(o.a)
print(o.b)

o = Manager()
print(o.a)
print(o.b)
print(o.c)
