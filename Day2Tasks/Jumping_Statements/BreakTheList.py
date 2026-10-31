#4. Write a program that searches for a number in a list and breaks the loop when found. 




a=[10,20,30,40,50]
num=int(input("Enter a number to break the loop:"))
for i in a:
    if a==num:
        break
    print(a)
