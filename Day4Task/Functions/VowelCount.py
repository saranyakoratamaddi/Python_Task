#19. Write a function that takes a string as input and returns the number of vowels. 





def vowelscount(string):
    vowels="AEIOUaeiou"
    count=0
    for char in string:
        if char in vowels:
            count+=1
    return count
string=input("Enter a String:")
result=vowelscount(string)
print("Number of Vowels in the string is:",result)
    
