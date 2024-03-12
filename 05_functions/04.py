import math
radius = int(input("Enter the radius of the circle: "))

def circle_stats(radius):
        area = math.pi * radius ** 2
        circumference  = 2 * math.pi * radius
        return (area, circumference)
    
a, c = circle_stats(radius)

print("Area:", a, "Circumference:", c)



