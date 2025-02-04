class TwoVector:
    
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
    def showTwo(self):
        print(f"x = {self.x}, y = {self.y}")
  
class ThreeVector(TwoVector):        
    def __init__(self, x,y,z):
        super().__init__(x,y)
        self.z = z
        
    def showThree(self):   
        print(f"x = {self.x}, y = {self.y}, z = {self.z}") 
        
       
a = TwoVector(1,2)
a.showTwo()        
b = ThreeVector(5,6,3)
b.showThree()
b.showTwo()