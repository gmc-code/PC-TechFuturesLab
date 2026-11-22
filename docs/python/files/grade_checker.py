# grade_checker.py
# Algorithm: turn a test mark (out of 100) into a grade.

mark = int(input("Enter the test mark (0-100): "))

if mark < 0 or mark > 100:
    print("That is not a valid mark.")
elif mark >= 80:
    print("Grade: A")
elif mark >= 65:
    print("Grade: B")
elif mark >= 50:
    print("Grade: C")
else:
    print("Grade: D")
