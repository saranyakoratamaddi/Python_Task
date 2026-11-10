#2. Write a program that uses random.choice() to randomly select a student from a list and display: 
#"The selected student for presentation is: <name>". 



import random
std=["Ram","Radha","Kiran","Avi","Bharath"]
selectstd=random.choice(std)
print(f"The selected students for the presentation is:{selectstd}")
