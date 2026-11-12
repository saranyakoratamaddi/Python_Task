#3. Palindrome Number 
#Question: Write a program to check whether a number is a Palindrome. 
#Definition: A number is a Palindrome if it reads the same forward and backward. 
#Example: 
#Number = 121 
#Reverse = 121 
#Output: 121 is a Palindrome number.




num=int(input("Enter a Number:"))
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if rev==num:
    print(f"Yes {num} is Polindrom")
else:
    print(f"No {num} is not Polindrom")
