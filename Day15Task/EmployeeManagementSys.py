#5. Employee Management System (OOP + File + Dict) 
#Scenario: 
#Manage employee data. 
#Task: 
#● Create a class Employee 
#● Store employees in a dictionary 
#● Save data to a file 
#● Use exception handling for invalid salary input 
#● Use loop to display all employees





class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
    def to_dict(self):
        return{"Employee":self.emp_id,"Name":self.name,"Salary":salary}
employees={}
while True:
    print("Employee Management System")
    print("1.Add Employee")
    print("2.Display all Employees")
    print("3.Save Employees to File")
    print("4.Exit")
    choice=input("Enter your choice")
    if choice=="1":
        emp_id=input("Enter employee id")
        name=input("Enter name of the Employee")
        try:
            salary=float(input("Enter employee salary:"))
            employee=Employee(emp_id,name,salary)
            employees[emp_id]=employee
            print("Employees added sucussfully")
        except ValueError:
            print("Invalid salary:")
    elif choice=="2":
        if not employees:
            print("No Employee found")
        else:
            print("Employee details")
            for emp_id,emp in employees.item():
                  print("EmployeeId:",emp.emp_id)
                  print("Name:",emp.name)
                  print("Salary:",emp.salary)
    elif choice=="3":
        try:
            with open("employees.txt","w")as file:
                for emp in employees.values():
                    file.write(f"{emp.emp_id},{emp.name},{emp.salary}")
                print("Employee data saved Successfully")
        except IOError:
            print("Error while saving the file:")
    elif choice=="4":
        print("Thank You")
        break
    else:
        print("Invalid choice:")
        
