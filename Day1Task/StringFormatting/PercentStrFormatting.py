#8. Display a percentage using string formatting.   


marks=int(input("Enter Marks:"))
percent=(marks/600)*100
print(f"Marks of the student:{percent:%}")
print(f"Marks of the student:{percent:.2%}")
