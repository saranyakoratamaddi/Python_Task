#4. Write a recursive function to reverse a string. 



def revstr(s):
    if len(s)<1:
        return s
    else:
        return revstr(s[1:])+s[0]
s=input("Enter a String:")
result=revstr(s)
print("The Reversed String is",result)
