#9. Online Shopping System (Multilevel Inheritance) 
#An e-commerce company organizes products using multiple levels. Create classes Product → ElectronicProduct → MobilePhone using multilevel inheritance and 
#display product details.





class Products:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class ElectronicProduct(Products):
    def __init__(self,name,price,brand,warranty):
        Products.__init__(self,name,price)
        self.brand=brand
        self.warranty=warranty
class MobilePhone(ElectronicProduct):
    def __init__(self,name,price,brand,warranty,ram,storage):
        ElectronicProduct.__init__(self,name,price,brand,warranty)
        self.ram=ram
        self.storage=storage
    def display(self):
        print("Product Name:",self.name)
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Warranty:",self.warranty)
        print("Ram:",self.ram)
        print("Storage:",self.storage)
phone=MobilePhone("OnePlus15r",70000,"Oneplus","2Years","16GB","512GB")
phone.display()
    
        
    
        
    
