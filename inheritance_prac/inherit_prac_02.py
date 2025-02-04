class Employee:
    salary = 500
    increment = 20
    
    @property
    def displaySalary(self):
        return (self.salary+ self.salary * (self.increment/100))
    
    @displaySalary.setter
    def salaryAfterIncrement(self, value):
         self.increment = ((value/self.salary) -1) * 100
     
    
    
    

e = Employee()
e.salaryAfterIncrement = 600
print(e.increment)
