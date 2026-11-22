# tk_temperature.py
# Small app 1: convert Celsius to Fahrenheit, with input validation.

# 1. IMPORTS
import tkinter as tk


# 3. FUNCTIONS
def celsius_to_fahrenheit(celsius):
    """Return the temperature in Fahrenheit."""
    return celsius * 9 / 5 + 32


def convert():
    """Read the Entry, convert it and show the answer."""
    text = celsius_entry.get()
    try:
        celsius = float(text)
    except ValueError:
        result_label.config(text="Please type a number.", fg="red")
        return

    fahrenheit = celsius_to_fahrenheit(celsius)
    result_label.config(text=f"{celsius:.1f} °C = {fahrenheit:.1f} °F", fg="black")


# 4. TKINTER WIDGETS
root = tk.Tk()
root.title("Temperature converter")

tk.Label(root, text="Celsius:").grid(row=0, column=0, padx=10, pady=10)

celsius_entry = tk.Entry(root, width=10)
celsius_entry.grid(row=0, column=1, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=1, column=0, columnspan=3, pady=10)

# 5. MAIN LOOP
root.mainloop()
