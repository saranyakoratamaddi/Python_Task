#4. Write an expression using parentheses to change precedence.   


a=int(input("Enter a Value:"))
b=int(input("Enter an another value:"))
c=int(input("Enter third value:"))
d=int(input("Enter fourth value:"))
exp1=((a+d)*(b+c)/(a+b))+((a%c)*(d+a)*(c+d)+(a/b))
print("The epression1 using Parenthesis:",exp1)
exp2=((d**c)/(a+b))<=((a+b)*(b-c))==((a/b)+(b/c)*(d+c)-(a+c))
print("The Expression 2 using parenthesis:",exp2)
