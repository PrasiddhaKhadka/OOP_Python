class Employee:
    name = ""
    salary = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def showemployee(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")
        
        
class Programmer(Employee):
    def show(self):    
        print(f"The name of the programmer is {self.name} and the language is {self.language}")
        
    def showLanguage(self):
        print(f"The language of the programmer is {self.language}")    
        
        
e2 = Programmer("Rams", 100000)
 
print(e2.showemployee())