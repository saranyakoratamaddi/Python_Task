#Dictionary Sorting: Given a dictionary:
#```python
#students = {
#"Rahul": 85,"Amit": 92,"Priya": 78, "Sneha": 95}```
#Sort the dictionary based on marks in descending order and print the top two students.




students = {"Rahul": 85,"Amit": 92,"Priya": 78,"Sneha": 95}
print(students)
sortstd=sorted(students.items(),key=lambda x:x[1],reverse=True)
print("The sorted student list using marks:",sortstd)
for name,marks in sortstd:
    print(name,"",marks)
for name,marks in sortstd[:2]:
    print("Top two students are")
    print(name,"",marks)
    
 
