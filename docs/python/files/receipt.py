# receipt.py
# Variables and f-strings: work out the cost of a canteen order.

item = input("What would you like to order? ")
price = float(input("How much does it cost? $"))
quantity = int(input("How many would you like? "))

total = price * quantity

print()
print("----- RECEIPT -----")
print(f"Item:     {item}")
print(f"Price:    ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total:    ${total:.2f}")
print("-------------------")
