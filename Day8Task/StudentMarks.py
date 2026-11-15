#4. Student Marks File Analyzer 
#A teacher stores student marks in a file marks.txt in the format: 
#Name Marks 
#Example: 
#Rahul 80 
#Anita 90 
#Ravi 75 
#Write a Python program to:
#● Read the file 
#● Display all student records 
#● Calculate and display the average marks of the class.





file=open("marks.txt","r")
lines=file.readlines()
print("Student Records")
total=0
count=0
for line in  lines:
          print(line.strip())
          if line.strip()=="NameMarks":
              continue
          name,marks=line.split()
          total=total+int(marks)
          count=count+1
avg=total/count
print("Average Marks:",avg)
file.close()
          
