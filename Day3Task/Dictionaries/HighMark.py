#8. Write a program to find the student with the highest marks from a dictionary.




std={"kumar":55,"Bharath":87,"Raj":33,"Rahul":97,"Ajay":66}
print(std)
stdresult=max(std,key=std.get)
stdmark=std[stdresult]
print("Student Name:",std)
print("student with Highest marks:",stdresult)

