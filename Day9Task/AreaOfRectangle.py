#2. Rectangle Area Calculator (Constructor) 
#A geometry application needs to calculate the area of rectangles. Create a Rectangle class that uses a constructor to initialize length and width. Add a method to calculate 
#and display the area.




class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def display(self):
        area=self.length*self.width
        print("The Area of the Rectangle is:",area)
rect1=Rectangle(20,10)
rect1.display()
