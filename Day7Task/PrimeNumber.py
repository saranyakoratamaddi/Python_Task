#4. Prime Number 
#Question: Write a program to check whether a number is Prime. 
#Definition: A Prime number is a number that has only two factors: 1 and itself. 
#Example: 
#Number = 7 
#Output: 
#Factors = 1, 7 ."7 is a Prime number".




num=int(input("Enter a Number:"))
if num>1:
    for i in range(1,num):
        if num%i==0:
            print(f"No {num} is a not Prime Number")
            break
        else:
            print(f"Yes {num} is a Prime number")
