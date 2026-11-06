#5. Write a program to check whether a substring exists in a string. 



string="This is the Python session"
substr=input("Enter a substring:")
if substr in string:
    print(f"Yes substring {substr} is in String")
else:
    print(f"No {substr} is not in the String")
