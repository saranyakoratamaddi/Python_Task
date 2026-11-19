#5. Vehicle Management System (Inheritance) 
#A transport company manages different vehicles. Create a base class Vehicle with attributes like brand and speed. Create derived classes Car and Bike that inherit from 
#Vehicle and display their details.





class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def display(self):
        print("Brand:",self.brand)
        print("Speed:",self.speed)
class Car(Vehicle):
    def __init__(self,brand,speed,fuel):
        Vehicle.__init__(self,brand,speed)
        self.fuel=fuel
    def display(self):
        Vehicle.display(self)
        print("Fuel:",self.fuel)
c1=Car("Swift",180,"Dissel")
c1.display()
    
        
    
    
