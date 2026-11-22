# times_table.py
# Iteration with a for loop: print a times table.

number = int(input("Which times table? "))

for i in range(1, 13):
    print(f"{i} x {number} = {i * number}")
