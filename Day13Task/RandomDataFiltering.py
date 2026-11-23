#8. Random Data & Filtering 
#Generate random numbers: 
#nums = np.random.randint(1, 100, 10) 
#Task: 
#● Filter values that are divisible by 5 
#● Return sorted result.



import random
import numpy as np
nums = np.random.randint(1, 100, 10)
div=nums[nums%5==0]
result=np.sort(div)
print(nums)
print("Filtered and sorted:",result)
