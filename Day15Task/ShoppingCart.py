#3. Shopping Cart System 
#Scenario: A user adds items to a shopping cart. 
#Task: 
#● Store items in a list 
#● Convert to set to remove duplicates 
#● Use loop + condition to calculate total cost 
#● Handle invalid input using try-except





cart_items=[]
unique_items=set()
while True:
    item=input("Enter an Item name")
    if item.lower()=="done":
        break
    if item in unique_items:
        print("Items already exist in cart")
        continue
    try:
        price=float(input("Enter item price:"))
        if price<=0:
            print("Please Enter valid price:")
            continue
        cart_item.append((item,price))
        unique_items.add(item)
        print("Item added sucessfully")
    except ValueError:
        print("Invalid input please entre a number")
total_cost=0
print("Shopping cart")
for item,price in cart_items:
    print(item,":",price)
    total_cost+=price
print("TotalCost",total_cost)
print("TotalItems:",unique_items)
