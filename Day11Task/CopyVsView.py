#13. Copy vs View Behavior in Data Processing 
#Scenario: 
#A dataset: 
#[10, 20, 30, 40] 
#Task: 
#● Create a copy of the array. 
#● Modify the original array. 
#● Show that the copy does not change. 
#● Repeat using view() and observe the difference.





import numpy as np
arr=np.array([10, 20, 30, 40])
print(arr)
arr_copy=arr.copy()
arr[0]=5
print("copied array:",arr_copy)
print("Array after updating a value:",arr)
arr=np.array([10, 20, 30, 40])#using view so recreating the original array
print("****View Array****")
print("Given Array",arr)
arr_view=arr.view()
arr[0]=5
print("Original array",arr)
print("View array",arr_view)

