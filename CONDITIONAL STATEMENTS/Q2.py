# 2. Traffic Light Simulation
# Problem: Write a program that simulates a traffic light. The program should output a
# message based on the current light:

# Red   : "Stop!"
# Yellow: "Prepare to stop"
# Green : "Go!"

# Jainam Shah


color = input("Enter the color of traffic light: ")
if color == "Red":
    print("Light: Red - Stop!")
elif color == "Yellow":
    print("Light: Yellow - Prepare to stop.")
elif color == "Green":
    print("Light: Green - Go!")
else:
    print("Invalid Input")