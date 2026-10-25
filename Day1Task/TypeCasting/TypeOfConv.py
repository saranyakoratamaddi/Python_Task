#10. Write a program to display the type of converted variable. 


intval=989898
a=float(intval)
floatval=6543.90
b=str(floatval)
strval="56565"
c=int(strval)
print("Converted int to float value is:",a,type(a))
print("Converted float to string value is:",b,type(b))
print("Converted string to integer value is:",c,type(c))
