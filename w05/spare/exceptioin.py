import math

try:
    x = int(input("Enter a number: "))
    result = math.sqrt(x)
    print(f"The square root of {x} is {result}")
except Exception as e:
    print("Please enter a valid number.")
    print(f"An error occurred: {e}")
