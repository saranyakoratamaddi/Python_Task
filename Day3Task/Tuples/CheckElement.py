#4. Write a program to check whether an element exists in a tuple. 



tup=(10,20,30,40,50)
n=int(input("Enter a number:"))
if n in tup:
    print(f"yes {n} is in the Tuple")
else:
    print(f"No {n} is not in the Tuple:")
