# cart is a variable containing list of turple that contain item and price

cart = []

def add_to_cart():
    item_name = input("What item would you like to add? ")
    item_price = float(input(f"What is the price of '{item_name}'? "))

    cart.append((item_name, item_price))

    print(f"'{item_name}' has been added to the cart.")

def remove_from_cart():
    if cart:
        print("\nThe contents of the shopping cart are:")
        for idx, item in enumerate(cart, 1):
            print(f"{idx}. {item[0]} - ${item[1]:.2f}")
        
        item_num = int(input("\nWhich item would you like to remove? "))

        if 1 <= item_num <= len(cart):
            removed_item = cart.pop(item_num - 1)
            print(f"'{removed_item[0]}' has been removed from the cart.")
        else:
            print("Invalid item number.")
    else:
        print("The cart is empty. No items to remove.")

while True:
    action = input("\nWould you like to add or remove an item? (add/remove/done): ").strip().lower()
    
    if action == 'add':
        add_to_cart()
    elif action == 'remove':
        remove_from_cart()
    elif action == 'done':
        break
    else:
        print("Invalid choice, please type 'add', 'remove', or 'done'.")

if cart:
    print("\nThe final contents of the shopping cart are:")
    for idx, item in enumerate(cart, 1):
        print(f"{idx}. {item[0]} - ${item[1]:.2f}")
    print(f"Total: ${sum(item[1] for item in cart):.2f}")
else:
    print("\nYour cart is empty.")
