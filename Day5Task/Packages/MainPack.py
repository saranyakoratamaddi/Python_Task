#A company wants to organize its Python code using packages. 
#Create a package named utilities that contains two modules: 
#● math_operations.py (functions for addition and multiplication) 
#● string_operations.py (functions to convert string to uppercase and count characters) 
#Write a Python program that imports the package and uses functions from both modules.




from utilities import math_operations,string_operations
a=56
b=90
text="Python"
sumresult=math_operations.add(a,b)
print(f"Addition of {a} and {b} is:",sumresult)
mulresult=math_operations.mul(a,b)
print(f"Multiplication of {a} and {b} is:",mulresult)
uppertext=string_operations.upper(text)
print("Upper Case of the given text is:",uppertext)
length=string_operations.countchar(text)
print(f"length of {text} is:",length)
