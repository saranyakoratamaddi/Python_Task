#10. Combine arithmetic and comparison operators in one expression. 


a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
c=int(input("Enter the third value:"))
exp1=((a+c)/(b-c)*a)>((b*a)**2)<=(b*c)
print("Expression1:",exp1)
exp2=((b%a)+(c+a))<(b+a)==(c*a)
print("Expression 2 ",exp2)
exp3=((a//c)*(b+a))>=((b+c)*a)!=(b*a)
print("Expression3:",exp3)




