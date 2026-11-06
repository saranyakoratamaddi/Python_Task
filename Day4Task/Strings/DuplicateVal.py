#10. Write a program to remove duplicate characters from a string. 


s=input("Enter a String:")
print(s)
result=""
for ch in s:
    if ch not in result:
        result+=ch
print("After Removing Duplicates form the string",result)
