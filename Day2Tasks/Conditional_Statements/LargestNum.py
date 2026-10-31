#3. Write a program to find the largest of three numbers using if-elif-else. 


a=int(input("Enter first Number:"))
b=int(input("Enter the second  Number:"))
c=float(input("Enter third Number:"))
if(a>=b) and (a>=c):
    print("The first number is the largest:",a)
elif(b>=a) and (b>=c):
    print("The second number is the largest number:",b)
else:
    print("The Third number is the largest number:",c)
