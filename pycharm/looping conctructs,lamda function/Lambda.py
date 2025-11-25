# Lambda functions
area_square = lambda x: x * x
area_rectangle = lambda l, w: l * w
area_triangle = lambda h, b: 0.5 * h * b

a = int(input("Enter the side of the square: "))
print("Area of the Square is:", area_square(a))

l = int(input("Enter the length of the rectangle: "))
w = int(input("Enter the width of the rectangle: "))
print("Area of the Rectangle is:", area_rectangle(l, w))

h = int(input("Enter the height of the triangle: "))
b = int(input("Enter the breadth of the triangle: "))
print("Area of the Triangle is:", area_triangle(h, b))
