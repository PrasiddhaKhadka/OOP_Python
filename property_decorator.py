class Employee:
    salary = 100000000000
        
    @classmethod   
    def displayEmployee(cls):
        print(f"The name of the employee ........ and the salary is {cls.salary}") 
        
    @property
    def displaySalary(self):  
        return f"The salary of the employee is {self.esalary}"
     
    @displaySalary.setter
    def displaySalary(self, value):  self.esalary = value
        

e = Employee()
e.displaySalary = 11111111111111
e.displayEmployee()
print("***********************")
print(e.displaySalary)
print("***********************")
print(e.salary)
print("***********************")

