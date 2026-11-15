#6. Employee Salary Management System 
#A company stores employee data in a file employees.txt in the format: 
#EmployeeName Salary 
#Example: 
#Ramesh 25000 
#Sita 30000 
#Arun 28000 
#Write a Python program that: 
#● Reads employee data from the file 
#● Displays all employee details 
#● Finds the employee with the highest salary 
#● Appends a new employee record to the file.




file=open("employees.txt","r")
content=file.readlines()
print(content)
file.close()
for n in content:
    name,salary=n.split()
    print("Name:",name,"Salary:",salary)
high_salary=0
high_emp=""
for n in content:
    name,salary=n.split()
    salary=int(salary)
    if salary>high_salary:
        high_salary=salary
        high_emp=name
print("\nEmployee with Highest Salary")
print("Name:",high_emp)
print("Salary:",high_salary)
print("Enter New Employee details:")
new_name=input("Enter Employee name:")
new_salary=int(input("Enter Employee Salary:"))
file=open("employee.txt","a")
file.write("New Employee details are added")
file.close()

