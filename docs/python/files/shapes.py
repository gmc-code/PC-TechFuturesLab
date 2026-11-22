# shapes.py
# Functions: reusable code with parameters and return values.


def rectangle_area(length, width):
    """Return the area of a rectangle."""
    return length * width


def triangle_area(base, height):
    """Return the area of a triangle."""
    return base * height / 2


def show_result(shape, area):
    """Print the area of a shape neatly."""
    print(f"The area of the {shape} is {area:.1f} square cm.")


# Main program
print("Area calculator")
choice = input("Rectangle or triangle? ").lower()

if choice == "rectangle":
    length = float(input("Length (cm): "))
    width = float(input("Width (cm): "))
    show_result("rectangle", rectangle_area(length, width))
elif choice == "triangle":
    base = float(input("Base (cm): "))
    height = float(input("Height (cm): "))
    show_result("triangle", triangle_area(base, height))
else:
    print("Sorry, I only know rectangles and triangles.")
