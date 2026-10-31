#5. Write a program to assign grades based on marks (for example: A, B, C, Fail). 


marks=int(input("Enter the Marks:"))
if marks>=90:
    print("You scored A Grade")
elif marks>=70:
    print("you scored B Grsde")
elif marks>=60:
    print("You scored C Grade")
else:
    print("You are Filed")
