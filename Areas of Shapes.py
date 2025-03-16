import math

# Calculating the area of a square

square_side = input(f"What is the lenth of one side of the square?")
square_side = float(square_side)
square_area = square_side * square_side
square_side_meters = float(square_area)/100
square_area_meters = square_side_meters * square_side_meters
print(f"The area of the square is {square_area}cms or {square_area_meters}meters")

# Calcualating the area of a rectangle

rectangle_length = input(f"What is the length of the rectangle?")
rectangle_length = float(rectangle_length)
rectangle_width = input(f"What is the width of the rectangle?")
rectangle_width = float(rectangle_width)
rectangle_area = rectangle_length * rectangle_width
print(f"The area of the rectangle is {rectangle_area}")

# Calculating the area of a circle

circle_radius = input(f"What is the radius of the circle?")
circle_radius = float(circle_radius)
circle_area = (math.pi * circle_radius) * circle_radius
print(f"The area of the circle is {circle_area}")


