# pizza_orders_starter.py
# A pizza ordering app using Tkinter.
# Starting point for the Python GUI project: change it into your own ordering app.

# =============================================================
# 1. IMPORTS
# =============================================================
import tkinter as tk
from tkinter import messagebox

# =============================================================
# 2. DATA
# =============================================================
# Nested dictionary: each pizza has its own dictionary of details
PIZZAS = {
    "Margherita": {"price": 12.00, "toppings": "tomato, mozzarella, basil"},
    "Pepperoni": {"price": 14.00, "toppings": "tomato, mozzarella, pepperoni"},
    "Hawaiian": {"price": 14.00, "toppings": "tomato, mozzarella, ham, pineapple"},
    "Vegetarian": {"price": 13.00, "toppings": "tomato, mozzarella, capsicum, mushroom, olives"},
}

# Size multipliers: a large pizza costs 1.3 times the medium price
SIZES = {"Small": 0.8, "Medium": 1.0, "Large": 1.3}

QUANTITIES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List of orders. Each order is a dictionary.
orders = []


# =============================================================
# 3. FUNCTIONS
# =============================================================
def calculate_cost(pizza, size, quantity):
    """Return the cost of an order line."""
    price = PIZZAS[pizza]["price"]
    return price * SIZES[size] * quantity


def show_toppings():
    """Show the toppings for the pizza that is selected."""
    pizza = pizza_var.get()
    toppings_label.config(text="Toppings: " + PIZZAS[pizza]["toppings"])


def add_order():
    """Check the inputs, then add the order to the list."""
    customer = customer_entry.get().strip()
    pizza = pizza_var.get()
    size = size_var.get()
    quantity = quantity_var.get()

    if customer == "":
        messagebox.showerror("Input error", "Please enter the customer name.")
        customer_entry.config(bg="pink")
        return

    customer_entry.config(bg="white")
    order = {
        "customer": customer,
        "pizza": pizza,
        "size": size,
        "quantity": quantity,
        "cost": calculate_cost(pizza, size, quantity),
    }
    orders.append(order)
    quantity_var.set(1)
    update_display()


def update_display():
    """Show every order in the Listbox and update the total."""
    orders_listbox.delete(0, tk.END)
    total = 0
    for order in orders:
        line = f"{order['customer']}: {order['quantity']} x {order['size']} {order['pizza']}  ${order['cost']:.2f}"
        orders_listbox.insert(tk.END, line)
        total = total + order["cost"]
    total_label.config(text=f"Total: ${total:.2f}")


def delete_order():
    """Delete the order selected in the Listbox."""
    selected = orders_listbox.curselection()
    if len(selected) == 0:
        messagebox.showinfo("Delete order", "Click an order in the list first.")
        return
    position = selected[0]
    orders.pop(position)
    update_display()


def clear_orders():
    """Remove every order after checking with the user."""
    if len(orders) == 0:
        return
    if messagebox.askyesno("Clear orders", "Delete ALL orders?"):
        orders.clear()
        update_display()


# =============================================================
# 4. TKINTER WIDGETS
# =============================================================
root = tk.Tk()
root.title("Pizza orders")
root.configure(padx=15, pady=15)

title_label = tk.Label(root, text="Pizza orders", font=("Arial", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

# Customer name
tk.Label(root, text="Customer:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
customer_entry = tk.Entry(root, width=25)
customer_entry.grid(row=1, column=1, columnspan=2, sticky="w", padx=5, pady=5)

# Pizza types (Radiobuttons made from the dictionary keys)
tk.Label(root, text="Pizza:").grid(row=2, column=0, sticky="ne", padx=5, pady=5)
pizza_frame = tk.Frame(root)
pizza_frame.grid(row=2, column=1, sticky="w", padx=5, pady=5)
pizza_var = tk.StringVar(value="Margherita")
for pizza in PIZZAS:
    price = PIZZAS[pizza]["price"]
    tk.Radiobutton(pizza_frame, text=f"{pizza} (${price:.2f})", variable=pizza_var,
                   value=pizza, command=show_toppings).pack(anchor="w")

# Sizes (Radiobuttons)
size_frame = tk.Frame(root)
size_frame.grid(row=2, column=2, sticky="nw", padx=5, pady=5)
tk.Label(size_frame, text="Size:").pack(anchor="w")
size_var = tk.StringVar(value="Medium")
for size in SIZES:
    tk.Radiobutton(size_frame, text=size, variable=size_var, value=size).pack(anchor="w")

# Toppings
toppings_label = tk.Label(root, text="", fg="grey30", wraplength=380, justify="left")
toppings_label.grid(row=3, column=0, columnspan=3, sticky="w", padx=5)

# Quantity (OptionMenu)
tk.Label(root, text="Quantity:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
quantity_var = tk.IntVar(value=1)
quantity_menu = tk.OptionMenu(root, quantity_var, *QUANTITIES)
quantity_menu.grid(row=4, column=1, sticky="w", padx=5, pady=5)

# Add order button
add_button = tk.Button(root, text="Add order", width=15, command=add_order)
add_button.grid(row=5, column=1, sticky="w", padx=5, pady=10)

# Orders list
orders_listbox = tk.Listbox(root, width=55, height=8)
orders_listbox.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

# Total and buttons
total_label = tk.Label(root, text="Total: $0.00", font=("Arial", 14, "bold"))
total_label.grid(row=7, column=0, columnspan=2, sticky="w", padx=5, pady=5)

delete_button = tk.Button(root, text="Delete order", command=delete_order)
delete_button.grid(row=7, column=2, sticky="e", padx=5)

clear_button = tk.Button(root, text="Clear all", command=clear_orders)
clear_button.grid(row=8, column=2, sticky="e", padx=5, pady=5)

show_toppings()

# =============================================================
# 5. MAIN LOOP
# =============================================================
root.mainloop()
