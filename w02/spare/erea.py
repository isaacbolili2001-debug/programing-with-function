def main():
    length = get_positive_value("Enter the length of the rectangle: ")
    width = get_positive_value ("Enter the width of the rectangle: ")
    area = length * width
    print(f"The area of the rectangle is: {area}") 

def get_positive_value(prompt):
    number=""
    while not number.isdigit():
        number=input(prompt)
        if not number.isdigit():
            print("please enter a digit number")
    digit_number=float(number)
    while digit_number < 0:
        print("Please enter a positive value.")
        digit_number = float(input(prompt))
    return digit_number
   
main()  