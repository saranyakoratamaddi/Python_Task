#Q1: Develop a Python program to manage student marks for three subjects. Store the subject names in a tuple, maintain unique student names in a set, and store each student’s marks 
#in a list inside a dictionary where the key is the student name. Create user-defined 
#functions to add a student with marks, display all student records, and calculate the average 
#marks of a student. Implement a recursive function to calculate the total marks from the list of marks. The program should interact with the user through a simple menu. Also include 
#exception handling to handle ValueError (non-numeric marks input), ZeroDivisionError 
#(average calculation issues), TypeError (incorrect data type in marks), and NameError (when a student name entered does not exist in the diction









subjects=("English","math","science")
stdname=set()
students={}
def calculate_total(marks):
    if not marks:
        return 0
    return marks[0]+calculate_total(marks[1:])
def add_std():
    name=input("EnterStudent Name")
    if name in stdname:
        print(f"Student {name} is already exist")
        return
    mark=[]
    try:
        for subject in subjects:
            mark=float(input(f"Enter marks for {subjects}"))
            if mark<0 or mark>100:
                       raise ValueError("Marks Must b between 0 and 100")
            marks.appent(mark)
        stdname.add(name)
        students[name]=mark
        print("Student record added successfully")
    except valueError as ve:
            print("Value Error",ve)
def display():
    if not students:
        print("Student record not found")
        return
    print("-----All Studentn Records----")
    for name,mark in students.items():
        print("Student Name:",name)
    for i in range(len(subjects)):
        print(subjects[i],":",mark[i])
    total=calculate_total(mark)
    print("Total Marks:",total)
    print("Average marks:",total/len(subjects))
def average():
    try:
        name=input("Enter Student Name:")
        mark=students[name]
        total=calculate_total(mark)
        average=total/len(mark)
        print("Student name:",name)
        print("Total Marks:",total)
        print("Average Mark:",average)
    except KeyError:
        print("Student name does not exist")
while True:
    print("1.Add Student")
    print("2.Display Students")
    print("3.Calculate Average")
    print("4.Exit")
    choice=int(input("Enter your choice(1-4):"))
    if choice==1:
        add_std()
    elif choice==2:
        display()
    elif choice==3:
        average()
    elif choice==4:
        print("Exit")
    else:
        print("Invalid Choice:")
    
    
    
        
            
