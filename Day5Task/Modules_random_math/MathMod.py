#3. Write a Python program using the math module to calculate and display the square root, floor value, and ceiling value of a number entered by the user. 





import math
num=float(input("Enter a value:"))
squareval=math.sqrt(num)
floorval=math.floor(num)
ceilval=math.ceil(num)
print(f"The Square root of {num} is {squareval}")
print(f"The Floor Value of {num} is {floorval}")
print(f"The Ceiling Value of {num} is {ceilval}")
