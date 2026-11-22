# tk_counter.py
# A first Tkinter window: a Label and two Buttons that change a count.

# 1. IMPORTS
import tkinter as tk

# 2. VARIABLES
count = 0


# 3. FUNCTIONS
def add_one():
    """Add 1 to the count and update the label."""
    global count
    count = count + 1
    count_label.config(text=f"Count: {count}")


def reset():
    """Set the count back to 0."""
    global count
    count = 0
    count_label.config(text=f"Count: {count}")


# 4. TKINTER WIDGETS
root = tk.Tk()
root.title("Click counter")
root.geometry("300x150")

title_label = tk.Label(root, text="Click counter", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

count_label = tk.Label(root, text="Count: 0", font=("Arial", 14))
count_label.grid(row=1, column=0, columnspan=2, pady=5)

add_button = tk.Button(root, text="Add 1", width=10, command=add_one)
add_button.grid(row=2, column=0, padx=10, pady=10)

reset_button = tk.Button(root, text="Reset", width=10, command=reset)
reset_button.grid(row=2, column=1, padx=10, pady=10)

# 5. MAIN LOOP
root.mainloop()
