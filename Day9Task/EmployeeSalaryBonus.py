#17. Employee Bonus Calculator (Decorators & OOP) 
#A company wants to apply a bonus calculation automatically before displaying the salary. Create an Employee class and use a decorator that modifies the salary by 
#adding a bonus before displaying it.






def bonus(func):
    def wrapper(self):
        bonus=self.salary*0.30
        self.salary=self.salary+bonus
        func(self)
    return wrapper
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @bonus
    def display_salary(self):
        print("Employee Name:",self.name)
        print("Salary After Bonus:",self.salary)
name=input("Enter Employee name:")
salary=float(input("Enter Employee saalary:"))
emp=Employee(name,salary)
emp.display_salary()
    
