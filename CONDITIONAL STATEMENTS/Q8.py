# 8. Quadrant Finder
# Problem: Write a program that takes the coordinates of a point (x, y) and determines
# which quadrant the point lies in:
# Quadrant 1: x > 0 and y > 0
# Quadrant 2: x < 0 and y > 0
# Quadrant 3: x < 0 and y < 0
# Quadrant 4: x > 0 and y < 0
# Origin: x == 0 and y == 0
# On x-axis: y == 0 and x != 0
# On y-axis: x == 0 and y != 0

# Jainam Shah

try:
    x = int(input("Enter x-coordinate: "))
    y = int(input("Enter y-coordinate: "))
except ValueError:
    print("Invalid input! Please enter a valid numerical value.")
else:
    if x > 0 and y > 0:
        print("Quadrant 1")
    elif x < 0 and y > 0:
        print("Quadrant 2")
    elif x < 0 and y < 0:
        print("Quadrant 3")
    elif x > 0 and y < 0:
        print("Quadrant 4")
    elif x == 0 and y == 0:
        print("Origin")
    elif x == 0:
        print("On the y-axis")
    else:
        print("On the x-axis")