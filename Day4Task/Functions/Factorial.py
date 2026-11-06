#16. Write a function that returns the factorial of a number. 




def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
num=int(input("Enter a Number"))
if num < 0:
    print("Negetive numbers are not allowed")
else:
    result=fact(num)
    print(f"Factorial of {num} is:",result)

