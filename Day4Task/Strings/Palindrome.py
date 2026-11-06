#8. Write a program to check whether a string is a palindrome. 


s=input("Enter a string:")
rev=s[::-1]
if s==rev:
    print("The String is Palindrome")
else:
    print("The String is not a Palindrome")
