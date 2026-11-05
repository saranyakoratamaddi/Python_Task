#4. Write a program to check if an element exists in a set. 



vehicle={"car","bike","scooter","lorry","truck"}
elem=input("Enter a name:")
if elem in vehicle:
    print(f"Yes {elem} is in the set")
else:
    print(f"No {elem} is not in the set")
