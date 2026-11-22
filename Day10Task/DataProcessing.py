#10. Data Processing Pipeline 
#A data pipeline receives the following array: 
#[12, 7, 25, 3, 18, 10] 
#Scenario: 
#1. Convert the list into a NumPy array. 
#2. Sort the array. 
#3. Split the sorted array into two equal parts. 
#4. Calculate the sum of each part. 
#Output: 
#● Sorted array 
#● Two split arrays 
#● Sum of each part.





import numpy as np
data=[12, 7, 25, 3, 18, 10]
arr=np.array([12, 7, 25, 3, 18, 10])
print(arr)
sortedarr=np.sort(arr)
part1,part2=np.array_split(sortedarr,2)
sum1=np.sum(part1)
sum2=np.sum(part2)
print("Sorted Array:",sortedarr)
print("Two split arrays:",part1,part2)
print("Sum of each part",sum1,sum2)
