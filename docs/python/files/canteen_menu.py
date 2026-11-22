# canteen_menu.py
# Dictionaries, including a nested dictionary.

# A simple dictionary: item -> price
prices = {
    "toastie": 4.50,
    "wrap": 6.00,
    "juice": 3.00,
}

# A nested dictionary: each item has its own dictionary of details
menu = {
    "toastie": {"price": 4.50, "vegetarian": True, "stock": 12},
    "wrap": {"price": 6.00, "vegetarian": False, "stock": 8},
    "juice": {"price": 3.00, "vegetarian": True, "stock": 20},
}

print("Simple dictionary")
print(f"A wrap costs ${prices['wrap']:.2f}")

print()
print("MENU")
for item in menu:
    details = menu[item]
    if details["vegetarian"]:
        veg = "(V)"
    else:
        veg = ""
    print(f"{item.title():10} ${details['price']:.2f} {veg}")

choice = input("What would you like? ").lower()

if choice in menu:
    menu[choice]["stock"] = menu[choice]["stock"] - 1
    print(f"Enjoy your {choice}! {menu[choice]['stock']} left.")
else:
    print("Sorry, that is not on the menu.")
