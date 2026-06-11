import math
from datetime import date

current_date=date.today()

# Get the width of the tire from the user.
width = int(input("Enter the width of the tire in mm (ex 205): "))

# Get the aspect ratio of the tire from the user.
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))

# Get the diameter of the wheel from the user.
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Compute the volume of the tire.
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Display the volume of the tire.
print(f"The volume of the tire is {volume:.2f} liters.")

# open the file volume.txt for appending and write the tire information to the file.
with open("volume.txt", "a") as file:
    file.write(f"{current_date}| {width}| {aspect_ratio}| {diameter}| {volume:.2f}\n")
print("Success! Data saved to volume.txt")