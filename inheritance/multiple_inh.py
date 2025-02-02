class Employee:
    def __init__(self, name, salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        

class Programmer(Employee):
    def printLanguage(self):
        print(f"The language is {self.language}")
        
    
class Manager(Programmer, Employee):
    pass

obj = Manager("Rams", 100000,"Python")
obj.printLanguage()