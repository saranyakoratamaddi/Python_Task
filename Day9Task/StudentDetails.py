#1. Student Information System (Class & Object) 
#A school wants a program to store student details. Create a Student class with attributes such as name, roll number, and marks. Create objects for at least
#three students and display their details. 





class student:
    def __init__(self,name,roll_num,marks):
        self.name=name
        self.roll_num=roll_num
        self.marks=marks
    def display(self):
        print("Student name:",self.name)
        print("Roll Number:",self.roll_num)
        print("Marks:",self.marks)
s1=student("Kiran",1001,98)
s2=student("Ram",1002,87)
s3=student("Kumar",1003,76)
print("Student Details")
s1.display()
s2.display()
s3.display()
