



import Calculator
a=float(input("Enter a float value:"))
b=int(input("Enter b value:"))
print("****Given Calculations are:***")
print("Addition")
print("Substraction")
print("Multiplication")
print("Division")
choice=int(input("Enter your choice between 1 to 4:"))
if choice==1:
    print("Addition",Calculator.add(a,b))
elif choice==2:
    print("Substraction:",Calculator.sub(a,b))
elif choice==3:
    print("Multiplication:",Calculator.mul(a,b))
elif choice==4:
    print("Division:",Calculator.div(a,b))
else:
    print("Out of Choice")
  

