class Employee:
    name = "Ram"
    salary = 100000000000
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    @classmethod   
    def displayEmployee(cls):
        print(f"The name of the employee is {cls.name} and the salary is {cls.salary}") 
        
    @staticmethod
    def displaySalary():   
        print(f"The salary of the employee is {Employee.salary}")
        
        
        
e1 = Employee("John", 1000)
e1.displayEmployee()
e1.displaySalary()