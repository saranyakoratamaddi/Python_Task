#18. Write a function to find the sum of elements in a list using a user-defined function. 



def sum(number):
    total=0
    for num in number:
        total+=num
    return total
li=[10,20,30,40,50]
result=sum(li)
print("Sum of the Elements in the List is:",result)
