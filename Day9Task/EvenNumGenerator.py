#15. Infinite Even Number Generator (Generators) 
#Create a generator function that continuously generates even numbers starting from 2. The program should print the first N even numbers using tis Generator.





def even_number(n):
    for i in range(n):
        if i%2==0:
            yield i
n=int(input("Enter range of even numbers:"))
for num in even_number(n):
      print(num)
    
