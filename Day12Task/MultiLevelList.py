#6. Multi-Level List Transformation (Advanced List Comprehension) 
#A dataset contains: 
#data = [[1, 2, 3], [4, 5], [6]] 
#Task: 
#● Flatten the list using list comprehension. 
#● Then create a new list containing squares of only even numbers






data=[[1, 2, 3], [4, 5], [6]]
print(data)
flattened_data=[num for sublist in data for num in sublist]
print("Flattened Lst",flattened_data)
even_data=[num**2 for num in flattened_data if num%2==0]
print("Squares Of even numbers:",even_data)





