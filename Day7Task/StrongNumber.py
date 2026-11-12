#2. Strong Number 
#Question: Write a program to check whether a given number is a Strong number. 
#Definition: A Strong number is a number whose sum of factorial of digits is equal to the number itself. 
#Example: Number = 145 
#Calculation: 
#1! + 4! + 5! 
#= 1 + 24 + 120 
#= 145 
#Output: 145 is a Strong number.



import math
num=int(input("Enter a Number"))
temp=num
factsum=0
while temp>0:
    digit=temp%10
    factsum+=math.factorial(digit)
    temp//=10
if factsum==num and num>0:
    print(f"Yes {num} is a Strong number")
else:
    print(f"No {num} is not a Strong number")
