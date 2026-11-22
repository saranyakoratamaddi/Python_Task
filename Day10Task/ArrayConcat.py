#4. Combine Two Sensor Readings 
#Two sensors record readings during a test. 
#Scenario: 
#Sensor1 = [1, 20, 30] 
#Sensor2 = [40, 50, 60] 
#Task: 
#● Store both readings in NumPy arrays. 
#● Combine them into one array using NumPy concatenation






import numpy as np
arr1=np.array([1, 20, 30])
arr2=np.array([40, 50, 60])
print(arr1)
print(arr2)
result=np.concatenate((arr1,arr2))
print("Adding both Arrays:",result)
