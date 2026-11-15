#3. Grocery List Manager 
#A user wants to save grocery items in a file grocery.txt. Write a Python program that takes multiple items from the user and writes them into the file, with each item on a 
#new line.





file=open("grocery.txt","w")
n=int(input("How many items do you want to store :"))
for i in range(n):
    items=input("Enter the Item name:")
    file.write(items+"\n")
file.close()
print("The Items That are saved in the file are:")
file=open("grocery.txt","r")
print("Grocery List")
print(file.read())
file.close()
