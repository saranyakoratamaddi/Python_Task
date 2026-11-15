#1. Student Attendance Record 
#A teacher wants to store student attendance in a file named attendance.txt. Write a Python program that takes a student name as input and appends it to the file. Then 
#display the contents of the file.







student_name=input("Enter Student Name:")
file=open("attendance.txt","a")
file.write(student_name+"\n")
file.close()
print("Student Attendance saved successfully")
file=open("attendance.txt","r")
print("Student Attendance Record")
print(file.read())
file.close()

