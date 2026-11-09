#Given a list `[1, 2, 3, 2, 4, 1, 5, 3]`, remove duplicate elements while preserving the original order. Do not use `set()`.



li=[1,2,3,2,4,1,5,3]
emptyli=[]
for num in li:
    if num not in emptyli:
        emptyli.append(num)
print("The Original List is:",li)
print("The list after removing Duplicates:",emptyli)
