#9. Write a program to count the frequency of each character in a string. 


string=input("Enter a String:")
count={}
for char in string:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
print(count)
