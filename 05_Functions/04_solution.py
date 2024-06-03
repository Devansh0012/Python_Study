import math

def circle(r):
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    return area, circumference

r = int(input("Enter the radius of the circle: "))

print("The area and circumference of the circle is: ",circle(r))