#2. Random Number Analyzer 
#Scenario: 
#A system generates random numbers for testing. 
#Task: 
#● Use random to generate 10 numbers 
#● Store in a list 
#● Use loop + condition to count even/odd numbers 
#● Use set to remove duplicates





import random
numbers=[random.randint(1,20) for i in range(10)]
even=0
odd=0
for num in numbers:
    if num%2==0:
        even+=1
    else:
        odd+=1
unique_num=set(numbers)
print("Generated numbers:",numbers)
print("Even Count",even)
print("Odd count:",odd)
print("Unique numbers:",unique_num)
    
