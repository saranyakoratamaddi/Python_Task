#Common Elements Using Sets: Given two lists:
# ```python
#list1 = [1, 2, 3, 4, 5]
#list2 = [3, 4, 5, 6, 7]
#Find:
#* Common elements.
# * Elements present only in the first list.
#* All unique elements from both lists.



list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
print(list1)
print(list2)
set1=set(list1)#coverting lists into set 
set2=set(list2)
common=set1.intersection(set2)
print("common elements in set1 and set2 are:",common)
firstlist=set1.difference(set2)
print("Common Elements in the First list:",firstlist)
uniqueval=set1.union(set2)
print("All Unique values from the both the lists:",uniqueval)
