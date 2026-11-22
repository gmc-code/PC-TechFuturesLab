# movie_ticket.py
# Selection with logical operators: work out a movie ticket price.

age = int(input("How old are you? "))
day = input("What day is it? ").lower()

if age < 5:
    price = 0
elif age < 16 or age >= 65:
    price = 12
else:
    price = 18

# Tuesday is half-price day, but not for free tickets
if day == "tuesday" and price > 0:
    price = price / 2

if price == 0:
    print("Your ticket is free!")
else:
    print(f"Your ticket costs ${price:.2f}")
