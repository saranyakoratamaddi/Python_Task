#  Write a Python program that generates 20 random numbers between 1 and 200 using the random module and store them in a list. 
#Then using the math module, compute and display: 
#● Maximum value 
#● Minimum value 
#● Square root of the maximum number 
#● Logarithm of the minimum number



import random
import math
li=[random.randint(1,200)for i in range(20)]
print(li)
maxval=max(li)
print("The maximum value in the list is:",maxval)
minval=min(li)
print("Minimum value in the list is:",minval)
squareval=math.sqrt(maxval)
print("The Square root of maximum value is:",squareval)
logval=math.log(minval)
print("Logarithm of the minimum number is:",logval)
