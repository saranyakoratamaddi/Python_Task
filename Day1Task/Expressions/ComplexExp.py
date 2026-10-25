#8. Create a complex expression using multiple operators.   


marks1=float(input("Enter first year marks :"))
marks2=float(input("Enter second year marks:"))
result=((marks1+100)>=500 or marks2>=500) and (marks1<=300 or marks2<=300)
print("result of the student is:",result)
