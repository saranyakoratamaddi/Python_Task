#12. Random Dataset Normalization + Filtering 
#Scenario: 
#● Generate 8 random float values between 0 and 1. 
#Task: 
#1. Normalize by multiplying with 100 
#2. Filter values greater than 50 
#3. Sort the filtered values.



import random
data=[random.randint(1,100) for i in range(8)]
print("data",data)
normalized=[val*100 for val in data]
print("Normalized Data",normalized)
filtered=[val for val in normalized if val >50]
print("Filtered values",filtered)
sort=sorted(filtered)
print("sorted values",sort)
      
      
