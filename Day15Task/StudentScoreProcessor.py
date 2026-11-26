#1. Student Score Processor 
#Scenario: 
#A teacher stores student names and marks in a list of tuples. 
#Task: 
#● Convert data into a dictionary 
#● Use a loop + condition to find students scoring above 50 
#● Use math module to calculate average 
#● Store results in a text file





import math
std_data=[("Ram",76),("Krishna",76),("Rahul",97),("Karan",47)]
std_dict=dict(std_data)
above_50={}
for name,marks in std_dict.items():
    if marks>50:
        above_50[name]=marks
total=math.fsum(std_dict.values())
avg=total/len(std_dict)
with open("stdresult.txt","w")as file:
    file.write("All student scores:")
    for name,marks in std_dict.items():
        file.write(f" {name} : {marks}")
    file.write("Students scoring above 50:")
    for name,marks in above_50.items():
                file.write(f" {name} :{marks}")
    file.write(f"class average:{avg:.2f}")
print("Result successfully saved")
                           
                   






