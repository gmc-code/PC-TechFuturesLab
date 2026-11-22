# tk_tip_calculator.py
# Small app 2: split a restaurant bill, with Radiobuttons and an OptionMenu.

# 1. IMPORTS
import tkinter as tk

# 2. DATA
TIP_OPTIONS = {"No tip": 0, "10%": 0.10, "15%": 0.15}
PEOPLE = [1, 2, 3, 4, 5, 6, 7, 8]


# 3. FUNCTIONS
def calculate_share(bill, tip_rate, people):
    """Return the amount each person pays."""
    total = bill + bill * tip_rate
    return total / people


def calculate():
    """Read the inputs and show how much each person pays."""
    try:
        bill = float(bill_entry.get())
    except ValueError:
        result_label.config(text="Type the bill as a number, e.g. 84.50", fg="red")
        return

    if bill <= 0:
        result_label.config(text="The bill must be more than $0.", fg="red")
        return

    tip_rate = TIP_OPTIONS[tip_var.get()]
    people = people_var.get()
    share = calculate_share(bill, tip_rate, people)
    result_label.config(text=f"Each person pays ${share:.2f}", fg="black")


# 4. TKINTER WIDGETS
root = tk.Tk()
root.title("Bill splitter")

tk.Label(root, text="Bill total: $").grid(row=0, column=0, padx=10, pady=5, sticky="e")
bill_entry = tk.Entry(root, width=10)
bill_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

tk.Label(root, text="Tip:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tip_var = tk.StringVar(value="No tip")
column = 1
for option in TIP_OPTIONS:
    tk.Radiobutton(root, text=option, variable=tip_var, value=option).grid(row=1, column=column, sticky="w")
    column = column + 1

tk.Label(root, text="People:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
people_var = tk.IntVar(value=2)
people_menu = tk.OptionMenu(root, people_var, *PEOPLE)
people_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=4, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=4, column=0, columnspan=4, pady=10)

# 5. MAIN LOOP
root.mainloop()
