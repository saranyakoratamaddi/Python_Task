#3. Employee Data Copy Issue (Shallow vs Deep Copy) 
#A company stores employee data: 
#employees = [[101, "A"], [102, "B"], [103, "C"]] 
#Scenario: 
#● Create a shallow copy of the list. 
#● Modify one nested list (e.g., change "A" to "Z"). 
#● Observe changes in both lists. 
#Task: 
#● Explain why the change reflects in both. 
#● Fix it using deep copy.





import copy
employees = [[101, "A"], [102, "B"], [103, "C"]]
print("Given Employee data",employees)
shallow=copy.copy(employees)
shallow[0][1]="Z"
print("Original List",employees)
print("Shallow Copy",shallow)
print("***DeepCopy***")
employees = [[101, "A"], [102, "B"], [103, "C"]]
print("Given List",employees)
deep=copy.deepcopy(employees)
deep[0][1]="Z"
print("Original List after modifying",employees)
print("Deep Copy",deep)
