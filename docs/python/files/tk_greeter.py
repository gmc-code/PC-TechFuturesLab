# tk_greeter.py
# Entry, Text and messagebox: type a name and get a message.

# 1. IMPORTS
import tkinter as tk
from tkinter import messagebox


# 3. FUNCTIONS
def greet():
    """Read the name from the Entry and add a greeting to the Text box."""
    name = name_entry.get().strip()

    if name == "":
        messagebox.showerror("Missing name", "Please type your name first.")
        name_entry.config(bg="pink")
    else:
        name_entry.config(bg="white")
        message_text.insert(tk.END, f"Hello, {name}! Welcome to TechFuturesLab.\n")
        name_entry.delete(0, tk.END)


def clear_messages():
    """Delete everything in the Text box."""
    message_text.delete("1.0", tk.END)


# 4. TKINTER WIDGETS
root = tk.Tk()
root.title("Greeter")

name_label = tk.Label(root, text="Your name:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

name_entry = tk.Entry(root, width=25)
name_entry.grid(row=0, column=1, padx=10, pady=10)

greet_button = tk.Button(root, text="Greet me", command=greet)
greet_button.grid(row=0, column=2, padx=10, pady=10)

message_text = tk.Text(root, width=45, height=6)
message_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_messages)
clear_button.grid(row=2, column=2, padx=10, pady=10, sticky="e")

# 5. MAIN LOOP
root.mainloop()
