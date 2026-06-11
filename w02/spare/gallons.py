"""def main():
    starting_odometer_value=float(input("enter a sarting odometer value in miles: "))
    ending_odometer_value=float(input("enter an ending odometer value in miles: "))
    amount_of_gallons_used=float(input("enter the amount of gallons used: "))
    mpg=miles_per_gallon(ending_odometer_value,starting_odometer_value, amount_of_gallons_used)
    lp100k=liters_per_100km(mpg)
    print(f"miles per gallon: {mpg:.2f}")
    print(f"liters per 100 kilometers: {lp100k:.2f}")
    
def miles_per_gallon(ending_odometer_value,starting_odometer_value, amount_of_gallons_used):
    miles_driven=ending_odometer_value-starting_odometer_value
    mpg=miles_driven/amount_of_gallons_used
    return mpg
def liters_per_100km(mpg):
    lp100k=235.215/mpg
    return lp100k
main()
"""

def main():
    a=get_positive_number("please enter a value: ")
    b=get_positive_number("enter another value: ")
    sum=addition(a,b)
    substraction=sub(a,b)
    print(f"the sum of these two values is {sum:.2f} and their substraction is {substraction:.2f}")

def get_positive_number(prompt):
    result=""
    while not result.isdigit():
        result=input(prompt)
        if not result.isdigit():
            print("error, the value must be a digit")
    digit_number=float(result)
    while digit_number < 0:
        print("please the number must be positive")
        digit_number=float(input(prompt))
    return digit_number    

def addition(a,b):
    sum=a+b
    return sum
def sub(a,b):
    substraction=a-b
    return substraction

main()


