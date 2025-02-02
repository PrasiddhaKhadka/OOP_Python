class Car:
    model = "bmw"
    year = "2020"
    
    #dunder method is something which is automatically called
    def __init__(self, model, year) -> None:
        self.model = model
        self.year = year
        print("this is constructor")
    
    def getInfo(self):
        print(f"model is {self.model} and year is {self.year}")
        
    @staticmethod    
    def greet():
        print("hello")
        
       
car = Car("bmw", "2020") 
print(car.getInfo())
        