#Q2: Develop a Python program for a small shop to process customer purchases. Store product names and prices in a dictionary, items added to the cart in a list, product categories in a set, 
#and product details using tuples. Create functions to display products, add items to the cart, and calculate the total bill. Use a recursive function to compute the total price of all items in the cart. 
#Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError (calculation errors), TypeError (wrong data types in the cart), and NameError (when a product 
#name entered by the user does not exist)






products={"Pen":10,"Notebook":50,"Pencil":5}
categories={"Stationary","Writting","Books"}
product_details={"Pen","Notebook","Pencil"}
cart=[]
def display_product():
    print("Available Products:")
    for name,price in products.items():
        print(name,":",price)
def add_cart():
    try:
        name=input("Enter Product Name:")
        if name not in products:
            raise NameError("Product does not exist:")
        quantity=int(input("Enter Quantity:"))
        if quantity<=0:
            raise ValueError("Quantity must be greater than zero")
        price=proucts[name]
        cart.append((name,quantity,price))
        print("Item added to cart")
    except NameError as ne:
        print("NameError:",ne)
    except ValueError as ve:
        print("Value Error",ve)
    except TypeError:
        print("Type Error:Invalid data type")
def calculate_total(items):
    if not items:
        return 0
    try:
        name,quantity,price=item[0]
        return(quantity*price)+calculate_total(items[1:])
    except TypeError:
        print("Type Error")
        return 0
def calculate_average_price(total,items):
    try:
        total_items=sum(item[1] for item in items)
        average=total/total_items
        print(f"Average price per item:{average:.2f}")
    except ZeroDivisionError:
        print("ZeroDivisionError:Cannot calculate average of an empty cart")
    except TypeError:
        print("Type Error: Ivalid data type in cart items")
while True:
    print("1.Display Products") 
    print("2. Add Item to Cart ")
    print("3. View Total Bill ")
    print("4.Exit")
    choice=int(input("Enter your choice(1-4):"))
    if choice==1:
        display_product()
    elif choice==2:
        add_cart()
    elif choice==3:
        totalbill=calculate_total(cart)
        print("Total Bill",totalbill)
        calculate_average_price(totalbill,cart)
    elif choice==4:
        print("Exit")
        break
    else:
        print("Invalid choice")
        
          
