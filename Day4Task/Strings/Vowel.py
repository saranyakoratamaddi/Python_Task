#6. Write a program to count the number of vowels in a string. 



s=input("Enter a String:")
vowel="aeiou"
count=0
result=s.lower()
for char in result:
    if char in vowel:
        count+=1
print("Total Number of vowels in the string is :",count)
