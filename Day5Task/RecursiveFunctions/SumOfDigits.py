#3. Write a recursive function to calculate the sum of digits of a number. 



def sumnum(n):
    if n<10:
       return n
    else:
        return(n%10)+sumnum(n//10)
n=int(input("Enter a Number:"))
result=sumnum(n)
print(f"Sum of the digits in the number {n} is {result}")
