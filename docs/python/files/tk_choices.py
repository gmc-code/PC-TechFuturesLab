# tk_choices.py
# Listbox, Radiobutton and OptionMenu: build a smoothie order.

# 1. IMPORTS
import tkinter as tk

# 2. DATA
FRUITS = ["Banana", "Strawberry", "Mango", "Blueberry", "Pineapple"]
SIZES = ["Small", "Medium", "Large"]
MILKS = ["Dairy", "Soy", "Oat", "Almond"]


# 3. FUNCTIONS
def make_order():
    """Read every choice and show a summary."""
    selected = fruit_listbox.curselection()   # a tuple of positions, e.g. (0, 2)
    fruits = []
    for position in selected:
        fruits.append(fruit_listbox.get(position))

    if len(fruits) == 0:
        summary_label.config(text="Please choose at least one fruit.", fg="red")
        return

    size = size_var.get()
    milk = milk_var.get()
    fruit_text = ", ".join(fruits)
    summary_label.config(text=f"{size} {milk} smoothie with {fruit_text}", fg="black")


# 4. TKINTER WIDGETS
root = tk.Tk()
root.title("Smoothie bar")

# Listbox: choose one or more fruits
tk.Label(root, text="Fruits (choose one or more):").grid(row=0, column=0, sticky="w", padx=10)
fruit_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=5, exportselection=False)
for fruit in FRUITS:
    fruit_listbox.insert(tk.END, fruit)
fruit_listbox.grid(row=1, column=0, rowspan=3, padx=10, pady=5)

# Radiobuttons: choose exactly one size
tk.Label(root, text="Size:").grid(row=0, column=1, sticky="w")
size_var = tk.StringVar(value="Medium")
row = 1
for size in SIZES:
    tk.Radiobutton(root, text=size, variable=size_var, value=size).grid(row=row, column=1, sticky="w")
    row = row + 1

# OptionMenu: a drop-down list
tk.Label(root, text="Milk:").grid(row=0, column=2, sticky="w", padx=10)
milk_var = tk.StringVar(value=MILKS[0])
milk_menu = tk.OptionMenu(root, milk_var, *MILKS)
milk_menu.grid(row=1, column=2, padx=10, sticky="w")

order_button = tk.Button(root, text="Make my smoothie", command=make_order)
order_button.grid(row=4, column=0, columnspan=3, pady=10)

summary_label = tk.Label(root, text="", font=("Arial", 12))
summary_label.grid(row=5, column=0, columnspan=3, pady=10)

# 5. MAIN LOOP
root.mainloop()
