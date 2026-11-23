#6. Remove Outliers 
#Given data: 
#values = np.array([10, 12, 15, 18, 100, 14, 13]) 
#Task: 
#● Compute the mean and standard deviation 
#● Remove values that are more than 2 standard deviations form mean.




import numpy as np
values = np.array([10, 12, 15, 18, 100, 14, 13])
mean=np.mean(values)
std_dev=np.std(values)
filtered=values[np.abs(values-mean)<=2*std_dev]
print("Mean",round(mean,2))
print("Standard Deviation:",round(std_dev,2))
print("Filtered Values:",filtered)
