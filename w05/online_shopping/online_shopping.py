import csv
import os



def main():
    # Display login options
    login_list=["Sign up", "Login", "Exit"]
    online_shopping =[
    "Category", "View cart", "Remove a product", "Payment", "Exit"
]
    category_list=[
    "Electronics",
    "Fashion",
    "Food",
    "Gaming",
    "Books",
    "Home Appliances",
    "Toys",
    "Furniture",
    "Beauty",
    "Sports",
    "Accessories"
]
    

    user_choice=0
    
    print("\nThe Online Shopping System!")
    print("Please select an option:")
    print()

    # Print the login options
    for i, option in enumerate(login_list, start=1):
        print(f"{i}. {option}")

    # Get user input for login option
    user_choice = get_digital_number("\nPlease select an option (1-3): ")
    while user_choice != 3:
        if  user_choice >3 or user_choice <1:
            print("Invalid choice. Please select a valid option (1-3).")
            user_choice = get_digital_number("\nPlease select an option (1-3): ")


        # this is for the sign in option
        if user_choice == 1:
            username=sign_up("w05/online_shopping/connexion.csv")
            for i, option in enumerate(login_list, start=1):
                print(f"{i}. {option}")
            user_choice = get_digital_number("\nPlease select an option (1-3): ")   
        #this is for the login option
        elif user_choice == 2:
            if login("w05/online_shopping/connexion.csv"):
                print("\nWelcome To The Online Shopping System!")

                #print the online shopping menu.
                for i, online_shopping_option in enumerate(online_shopping, start=1):
                    print(f"{i}. {online_shopping_option}")
                user_choice = get_digital_number("Please select an option (1-5): ")
                # Loop until the user chooses to exit the online shopping menu
                while user_choice != 5:
                    if user_choice < 1 or user_choice > 5:
                        print("Invalid choice. Please select a valid option (1-5).")
                        user_choice = get_digital_number("Please select an option (1-5): ")
                    #The category option
                    if user_choice==1:
                        
                        # Print the category options
                        print("\nCategories")
                        for i, category in enumerate(category_list, start=1):
                            print(f"{i}. {category}")
                        user_choice = get_digital_number("Please select a category (1-11): ")
                        while user_choice != 11:
                            if user_choice < 1 or user_choice > 6:
                                print("Invalid choice. Please select a valid option (1-11).")
                                user_choice = get_digital_number("Please select a category (1-11): ")
                            # Show electronics products
                            if user_choice == 1:
                                
                                show_products_by_category("w05/online_shopping/online_shopping.csv", "Electronics")
                                #get the product from the user using the product id and the quantity
                                product_id = input("Enter the product ID you want to add to cart (or 0 to go back): ").strip().upper()

                                # Check if the user wants to go back to the category menu
                                if product_id == "0":
                                    break
                                # Validate product ID format (e.g., P01, P02, etc.)
                                if not product_id.startswith("P") or not product_id[1:].isdigit():
                                    print("Invalid product ID format. Please enter a valid product ID (e.g., P01).")
                                    continue

                                quantity = get_digital_number("Enter the quantity  (or 0 to go back): ")
                                if quantity == 0:
                                    continue
                                if quantity < 0:
                                    print("Invalid quantity. Please enter a positive number.") 
                                    continue
                                add_to_cart(
                                    "w05/online_shopping/online_shopping.csv",
                                    "w05/online_shopping/cart.csv", 
                                    product_id, 
                                    quantity
                                    )
                            
                            # Show fashion products
                            elif user_choice == 2:
                                show_products_by_category("w05/online_shopping/online_shopping.csv", "Fashion")
                                #get the product from the user using the product id and the quantity
                                product_id = input("Enter the product ID you want to add to cart (or 0 to go back): ").strip().upper()
                                # Check if the user wants to go back to the category menu
                                if product_id == "0":
                                    break
                                # Validate product ID format (e.g., P01, P02, etc.)
                                if not product_id.startswith("P") or not product_id[1:].isdigit():
                                    print("Invalid product ID format. Please enter a valid product ID (e.g., P01).")
                                    continue

                                quantity = get_digital_number("Enter the quantity  (or 0 to go back): ")
                                if quantity == 0:
                                    continue
                                if quantity < 0:
                                    print("Invalid quantity. Please enter a positive number.") 
                                    continue
                                add_to_cart(
                                    "w05/online_shopping/online_shopping.csv",
                                    "w05/online_shopping/cart.csv", 
                                    product_id, 
                                    quantity
                                    )
                            # Show books products
                            elif user_choice == 3:
                                show_products_by_category("w05/online_shopping/online_shopping.csv", "Books")
                                #get the product from the user using the product id and the quantity
                                product_id = input("Enter the product ID you want to add to cart (or 0 to go back): ").strip().upper()
                                # Check if the user wants to go back to the category menu
                                if product_id == "0":
                                    break
                                # Validate product ID format (e.g., P01, P02, etc.)
                                if not product_id.startswith("P") or not product_id[1:].isdigit():
                                    print("Invalid product ID format. Please enter a valid product ID (e.g., P01).")
                                    continue

                                quantity = get_digital_number("Enter the quantity  (or 0 to go back): ")
                                if quantity == 0:
                                    continue
                                if quantity < 0:
                                    print("Invalid quantity. Please enter a positive number.") 
                                    continue
                                add_to_cart(
                                    "w05/online_shopping/online_shopping.csv",
                                    "w05/online_shopping/cart.csv", 
                                    product_id, 
                                    quantity
                                    )
                            # Show home appliances products
                            elif user_choice == 4:
                                show_products_by_category("w05/online_shopping/online_shopping.csv", "Gaming")
                                #get the product from the user using the product id and the quantity
                                product_id = input("Enter the product ID you want to add to cart (or 0 to go back): ").strip().upper()
                                # Check if the user wants to go back to the category menu
                                if product_id == "0":
                                    break
                                # Validate product ID format (e.g., P01, P02, etc.)
                                if not product_id.startswith("P") or not product_id[1:].isdigit():
                                    print("Invalid product ID format. Please enter a valid product ID (e.g., P01).")
                                    continue

                                quantity = get_digital_number("Enter the quantity  (or 0 to go back): ")
                                if quantity == 0:
                                    continue
                                if quantity < 0:
                                    print("Invalid quantity. Please enter a positive number.") 
                                    continue
                                add_to_cart(
                                    "w05/online_shopping/online_shopping.csv",
                                    "w05/online_shopping/cart.csv", 
                                    product_id, 
                                    quantity
                                    )
                            # Show gaming products
                            elif user_choice == 5:
                                show_products_by_category("w05/online_shopping/online_shopping.csv", "Books")
                                #get the product from the user using the product id and the quantity
                                product_id = input("Enter the product ID you want to add to cart (or 0 to go back): ").strip().upper()
                                # Check if the user wants to go back to the category menu
                                if product_id == "0":
                                    break
                                # Validate product ID format (e.g., P01, P02, etc.)
                                if not product_id.startswith("P") or not product_id[1:].isdigit():
                                    print("Invalid product ID format. Please enter a valid product ID (e.g., P01).")
                                    continue

                                quantity = get_digital_number("Enter the quantity  (or 0 to go back): ")
                                if quantity == 0:
                                    continue
                                if quantity < 0:
                                    print("Invalid quantity. Please enter a positive number.") 
                                    continue
                                add_to_cart(
                                    "w05/online_shopping/online_shopping.csv",
                                    "w05/online_shopping/cart.csv", 
                                    product_id, 
                                    quantity
                                    )
                                
                            elif user_choice == 6:
                                show_products_by_category("w05/online_shopping/online_shopping.csv", "Home Appliances")
                                #get the product from the user using the product id and the quantity
                                product_id = input("Enter the product ID you want to add to cart (or 0 to go back): ").strip().upper()
                                # Check if the user wants to go back to the category menu
                                if product_id == "0":
                                    break
                                # Validate product ID format (e.g., P01, P02, etc.)
                                if not product_id.startswith("P") or not product_id[1:].isdigit():
                                    print("Invalid product ID format. Please enter a valid product ID (e.g., P01).")
                                    continue

                                quantity = get_digital_number("Enter the quantity  (or 0 to go back): ")
                                if quantity == 0:
                                    continue
                                if quantity < 0:
                                    print("Invalid quantity. Please enter a positive number.") 
                                    continue
                                add_to_cart(
                                    "w05/online_shopping/online_shopping.csv",
                                    "w05/online_shopping/cart.csv", 
                                    product_id, 
                                    quantity
                                    )

                            elif user_choice == 7:
                                show_products_by_category("w05/online_shopping/online_shopping.csv", "Toys")
                                #get the product from the user using the product id and the quantity
                                product_id = input("Enter the product ID you want to add to cart (or 0 to go back): ").strip().upper()
                                # Check if the user wants to go back to the category menu
                                if product_id == "0":
                                    break
                                # Validate product ID format (e.g., P01, P02, etc.)
                                if not product_id.startswith("P") or not product_id[1:].isdigit():
                                    print("Invalid product ID format. Please enter a valid product ID (e.g., P01).")
                                    continue

                                quantity = get_digital_number("Enter the quantity  (or 0 to go back): ")
                                if quantity == 0:
                                    continue
                                if quantity < 0:
                                    print("Invalid quantity. Please enter a positive number.") 
                                    continue
                                add_to_cart(
                                    "w05/online_shopping/online_shopping.csv",
                                    "w05/online_shopping/cart.csv", 
                                    product_id, 
                                    quantity
                                    )

                            elif user_choice == 8:
                                show_products_by_category("w05/online_shopping/online_shopping.csv", "Furniture")
                                #get the product from the user using the product id and the quantity
                                product_id = input("Enter the product ID you want to add to cart (or 0 to go back): ").strip().upper()
                                # Check if the user wants to go back to the category menu
                                if product_id == "0":
                                    break
                                # Validate product ID format (e.g., P01, P02, etc.)
                                if not product_id.startswith("P") or not product_id[1:].isdigit():
                                    print("Invalid product ID format. Please enter a valid product ID (e.g., P01).")
                                    continue

                                quantity = get_digital_number("Enter the quantity  (or 0 to go back): ")
                                if quantity == 0:
                                    continue
                                if quantity < 0:
                                    print("Invalid quantity. Please enter a positive number.") 
                                    continue
                                add_to_cart(
                                    "w05/online_shopping/online_shopping.csv",
                                    "w05/online_shopping/cart.csv", 
                                    product_id, 
                                    quantity
                                    )


                            elif user_choice == 9:
                                show_products_by_category("w05/online_shopping/online_shopping.csv", "Beauty")
                                #get the product from the user using the product id and the quantity
                                product_id = input("Enter the product ID you want to add to cart (or 0 to go back): ").strip().upper()
                                # Check if the user wants to go back to the category menu
                                if product_id == "0":
                                    break
                                # Validate product ID format (e.g., P01, P02, etc.)
                                if not product_id.startswith("P") or not product_id[1:].isdigit():
                                    print("Invalid product ID format. Please enter a valid product ID (e.g., P01).")
                                    continue

                                quantity = get_digital_number("Enter the quantity  (or 0 to go back): ")
                                if quantity == 0:
                                    continue
                                if quantity < 0:
                                    print("Invalid quantity. Please enter a positive number.") 
                                    continue
                                add_to_cart(
                                    "w05/online_shopping/online_shopping.csv",
                                    "w05/online_shopping/cart.csv", 
                                    product_id, 
                                    quantity
                                    )



                            elif user_choice == 10:
                                show_products_by_category("w05/online_shopping/online_shopping.csv", "Sports")
                                #get the product from the user using the product id and the quantity
                                product_id = input("Enter the product ID you want to add to cart (or 0 to go back): ").strip().upper()
                                # Check if the user wants to go back to the category menu
                                if product_id == "0":
                                    break
                                # Validate product ID format (e.g., P01, P02, etc.)
                                if not product_id.startswith("P") or not product_id[1:].isdigit():
                                    print("Invalid product ID format. Please enter a valid product ID (e.g., P01).")
                                    continue

                                quantity = get_digital_number("Enter the quantity  (or 0 to go back): ")
                                if quantity == 0:
                                    continue
                                if quantity < 0:
                                    print("Invalid quantity. Please enter a positive number.") 
                                    continue
                                add_to_cart(
                                    "w05/online_shopping/online_shopping.csv",
                                    "w05/online_shopping/cart.csv", 
                                    product_id, 
                                    quantity
                                    )

                            elif user_choice == 11:
                                show_products_by_category("w05/online_shopping/online_shopping.csv", "Accessories")
                                #get the product from the user using the product id and the quantity
                                product_id = input("Enter the product ID you want to add to cart (or 0 to go back): ").strip().upper()
                                # Check if the user wants to go back to the category menu
                                if product_id == "0":
                                    break
                                # Validate product ID format (e.g., P01, P02, etc.)
                                if not product_id.startswith("P") or not product_id[1:].isdigit():
                                    print("Invalid product ID format. Please enter a valid product ID (e.g., P01).")
                                    continue

                                quantity = get_digital_number("Enter the quantity  (or 0 to go back): ")
                                if quantity == 0:
                                    continue
                                if quantity < 0:
                                    print("Invalid quantity. Please enter a positive number.") 
                                    continue
                                add_to_cart(
                                    "w05/online_shopping/online_shopping.csv",
                                    "w05/online_shopping/cart.csv", 
                                    product_id, 
                                    quantity
                                    )                            
                        # Exit category menu
                        print("Exiting category menu...")
                        print("\nOnline Shopping Menu:")
                        for i, online_shopping_option in enumerate(online_shopping, start=1):
                            print(f"{i}. {online_shopping_option}")
                        user_choice = get_digital_number("Please select an option (1-5): ")
                    #the view card option
                    elif user_choice==2:
                        print("you selected the view card option")
                        view_cart("w05/online_shopping/cart.csv")
                        print("\nOnline Shopping Menu:")
                        for i, online_shopping_option in enumerate(online_shopping, start=1):
                            print(f"{i}. {online_shopping_option}")
                        user_choice = get_digital_number("Please select an option (1-5): ") 
                    # the remove option
                    elif user_choice==3:
                        print("you selected the remove an item option")
                        print("Your Cart:")
                        view_cart("w05/online_shopping/cart.csv")
                        product_id = input("Enter the product ID you want to remove from cart (or 0 to go back): ").strip().upper()
                        if product_id == "0":
                            continue
                        remove_from_cart("w05/online_shopping/cart.csv", product_id)
                        print("\nOnline Shopping Menu:")
                        for i, online_shopping_option in enumerate(online_shopping, start=1):
                            print(f"{i}. {online_shopping_option}")
                        user_choice = get_digital_number("Please select an option (1-5): ")
                    #the payment option 
                    elif user_choice==4:
                        print("you selected the payment option")
                        payment("w05/online_shopping/cart.csv")
                        print("\nOnline Shopping Menu:")
                        for i, online_shopping_option in enumerate(online_shopping, start=1):
                            print(f"{i}. {online_shopping_option}")
                            
                        user_choice = get_digital_number("Please select an option (1-5): ")
                print("Exiting...")
                break 
            else:
                print("Login failed. Please try again.")

#get a valid digital number from the user
def get_digital_number(prompt):
    result = input(prompt)
    while not result.isdigit():
        print("Invalid input. Please enter a number.")
        result = input(prompt)
    return int(result)
"""#this function checks if the username already exists in the csv file
def username_check(filename):

    while True:
        username=input("Enter your username: ")
        exists=False

        try:
            with open(filename, "rt", newline="") as file:
                reader=csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    
                    if username == row[0]:
                        print("This username already exists. Please change the username")
                        exists=True
                        break
            
        except FileNotFoundError:
            return username           
        if exists:
            print("Please try again.")
        else:
            return username"""

#the sign up function

def sign_up(filename):
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()

    # Check if file exists
    file_exists = os.path.exists(filename)

    try:
        # Check if username already exists
        if file_exists:
            with open(filename, "rt", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == username:
                        print("Username already exists. Try another one.")
                        return False

        # Save new user
        with open(filename, "at", newline="") as file:
            writer = csv.writer(file)

            # Write header if file is new
            if not file_exists:
                writer.writerow(["username", "password"])

            writer.writerow([username, password])

        print("Signup successful!")
        return True

    except Exception as e:
        print("Error during signup:", e)
        return False



#the login function
def login(filename):
    
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    try:
        with open(filename, "rt") as file:
            reader=csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                if username == row[0] and password == row[1]:   
                    print("Login successful.")
                    print(f"Hello dear {username}!")
                    return True
            print("Invalid username or password.")
            return False
    except FileNotFoundError as e:
        print("Error: file.csv not found")
        print(f"Please try again.{e}")
        return False

#this function shows all categories in the csv file
def show_products_by_category(filename, selected_category):
    results = []
    try:
        with open(filename, "rt") as product:
            reader=csv.reader(product)
            next(reader)
            print(f"\nProducts in category: {selected_category}\n")
            for row in reader:
                if row[2] == selected_category:
                    print(f"{row[0]} - {row[1]} | ${row[3]} | Stock: {row[4]}")
                    results.append(row)
        return results            
    except FileNotFoundError as e:
        
        print("Error: file.csv not found")
        print(f"Please try again.{e}")
        return results
        

  
#this function adds the product to the cart if the quantity is available in stock
def add_to_cart(product_file, cart_file, product_id, quantity):
    try:
        with open(product_file, "rt") as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] == product_id:
                    product_name = row[1]
                    price = float(row[3])
                    stock_quantity = int(row[4])
                    if quantity > stock_quantity:
                        print("Not enough stock available.")
                        return False
                    else:
                        with open(cart_file, "at", newline="") as cart:
                            writer=csv.writer(cart)
                            writer.writerow([product_id, product_name, price, quantity])
                        print(f"{quantity} of {product_name} added to cart.")
                        return True
        print("Product not found.")
        return False
    except FileNotFoundError as e:
        print("Error: file.csv not found")
        print(f"Please try again.{e}")
        return False

#this function removes the product from the cart
def remove_from_cart(cart_file, product_id):
    try:
        with open(cart_file, "rt") as cart:
            reader=csv.reader(cart)
            cart_items = list(reader)

        updated_cart = []
        removed = False

        for item in cart_items:
            if item[0] != product_id:
                updated_cart.append(item)
            else:
                print(f"{item[1]} removed from cart.")
                removed = True    
        
        with open(cart_file, "wt", newline="") as cart:
            writer=csv.writer(cart)
            writer.writerows(updated_cart)
        return removed
    except FileNotFoundError as e:
        print("Error: file.csv not found")
        print(f"Please try again.{e}")
        return False
    
#this function shows the products in the cart
def view_cart(cart_file):
    try:
        with open(cart_file, "rt") as cart:
            reader=csv.reader(cart)
            print("\nYour Cart:")
            for row in reader:
                print(f"{row[0]}: {row[1]} - ${row[2]} x {row[3]}")
    except FileNotFoundError as e:
        print("Error: file.csv not found")
        print(f"Please try again.{e}")
        return False
    

#this function performs the payment and clears the cart
def payment(cart_file):
    try:
        with open(cart_file, "rt") as cart:
            reader = csv.reader(cart)
            items = list(reader)

        # Check if cart is empty
        if not items:
            print("Your cart is empty.")
            return False

        total = 0
        receipt_lines = []

        # Build receipt + calculate total
        for row in items:
            try:
                name = row[1]
                price = float(row[2])
                quantity = int(row[3])
                total += price * quantity
                receipt_lines.append(f"{name} - ${price} x {quantity}")
            except (ValueError, IndexError):
                print("Invalid data in cart file.")
                return False

        # Print receipt
        print("\nReceipt:")
        for line in receipt_lines:
            print(line)

        print(f"\nTotal amount: ${total:.2f}")
        print("Payment successful. Thank you for your purchase!")

        # Clear cart AFTER everything
        with open(cart_file, "wt", newline=""):
            pass

        return True

    except FileNotFoundError as e:
        print("Error: file.csv not found")
        print(f"Please try again. {e}")
        return False





    """try:
        product_dict={} 
        with open("w05/proposal_project/online_shopping.csv", "rt") as product:
            reader=csv.reader(product)
            
            next(reader)
            for row in reader:
                product_id=row[0]
                product_name=row[1]
                category=row[2]
                price=float(row[3])
                quantity=int(row[4])
                product_dict[product_id]={
                    "Name": product_name,
                      "Category":category, 
                      "Price":price, 
                      "Quantity":quantity
                }

        print(f"{"Number"} ...{'ID':}... {'Name':} ... {'Category':} ... {'Price':} ... {'Stock':}")
        print("_" * 55)
        for i, (product_id, info) in enumerate(product_dict.items(), start=1):
            print(f"{i:2}.| {product_id:<3} |{info['Name']:<5} ...{info['Category']:} ... ${info['Price']:<5} ...{info['Quantity']:} stocks")       
    
                

    except FileNotFoundError as e:
        print("Error: file.csv not found")"""


"""def user_connexion(filename):
    filename="user_connexion.csv"
    try:
        with open(filename, "wt") as file:
            writer=csv.writer(file)
    except FileExistsError:
        print("Error file not found")   """ 


















"""def read_shopping_file(product_id,product_name,category,price,quantity):
    with open("online_shopping.csv", "rt") as product:
        reader=csv.reader(product)
        product_dict={}
        for row in reader:
            product_id=row[0]
            product_name=row[1]
            category=row[2]
            price=row[3]
            quantity=row[4]
            product_dict[product_id]={
                "Name":product_name,
                "category":category,
                "price":price,
                "quantity":quantity
            }
            print(product_dict)"""

if __name__ == "__main__":
    main()