#7. Write a program to check whether a key exists in a dictionary. 



dict1={"Veggies":"Carrot","Fruits":"Apple","Flower":"Lilly"}
print(dict1)
val=input("Enter a Key value:")
if val in dict1:
    print(f"Yes {val} are in the Dictionary")
else:
    print(f"No {val} are not in the Dictionary")
