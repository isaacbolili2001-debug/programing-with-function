menus=[
    "Shopping", "Cart", "Inventory Management",
    "Customer Account","Statistics", "Settings", "Exit"
    ]
shopping=[
    "Electronics", "Fashion", "Food", "Gaming", "Books", "Exit"
]

electronics=[]
fashion=[]
food=[]
gaming=[]
books=[]

def main():
    username=input("Entrer votre nom: ")
    print(f"Welcome {username}")
  
    
   
    print("\nplease select one of the following: ")
    for i, j in enumerate(menus):
        print(f"{i+1} {j}")
    userinput=get_digit("\n choose one of them: ")
    while userinput!=7:
        if userinput >7 or userinput <1:
            print("Please choose a valid option")
            for i, j in enumerate(menus):
                print(f"{i+1} {j}")
            userinput=get_digit("\n choose one of them: ")
        if userinput==1:
            print("Welcome to the shopping card")
            print("\nPlease choose of of the following")
            for i, j in enumerate(shopping):
                print(f"{i+1}. {j}")
            userinput=get_digit("enter an option: ")
            if userinput==1:
                idp=get_digit("Enter the id of the product: ")
                name=input("Enter the name of the product: ")
                price=get_digit("Enter the price of the product: ")
                quantity=get_digit("Enter the quantity of the product: ")
                rate=price*quantity
                electronics.append((id, name, price, quantity, rate))
                print(f"Success, id {idp} has been added to the cart")
                for i, j in enumerate(shopping):
                    print(f"{i+1}. {j}")
                userinput=get_digit("choose of them: ")
            elif userinput==2:
                idp=get_digit("Enter the id of the product: ")
                name=input("Enter the name of the product: ")
                price=get_digit("Enter the price of the product: ")
                quantity=get_digit("Enter the quantity of the product: ")
                rate=price*quantity
                fashion.append((id, name, price, quantity, rate))
                print(f"Success, id {idp} has been added to the cart")
                for i, j in enumerate(shopping):
                    print(f"{i+1}. {j}")
                userinput=get_digit("choose of them: ")
            elif userinput==3:
                idp=get_digit("Enter the id of the product: ")
                name=input("Enter the name of the product: ")
                price=get_digit("Enter the price of the product: ")
                quantity=get_digit("Enter the quantity of the product: ")
                rate=price*quantity
                food.append((id, name, price, quantity, rate))
                print(f"Success, id {idp} has been added to the cart")
                for i, j in enumerate(shopping):
                    print(f"{i+1}. {j}")
                userinput=get_digit("choose of them: ")
            elif userinput==4:
                idp=get_digit("Enter the id of the product: ")
                name=input("Enter the name of the product: ")
                price=get_digit("Enter the price of the product: ")
                quantity=get_digit("Enter the quantity of the product: ")
                rate=price*quantity
                gaming.append((id, name, price, quantity, rate))
                print(f"Success, id {idp} has been added to the cart")
                for i, j in enumerate(shopping):
                    print(f"{i+1}. {j}")
                userinput=get_digit("choose of them: ")
            elif userinput==5:
                idp=get_digit("Enter the id of the product: ")
                name=input("Enter the name of the product: ")
                price=get_digit("Enter the price of the product: ")
                quantity=get_digit("Enter the quantity of the product: ")
                rate=price*quantity
                books.append((id, name, price, quantity, rate))
                print(f"Success, id {idp} has been added to the cart")
                for i, j in enumerate(shopping):
                    print(f"{i+1}. {j}")
                userinput=get_digit("choose of them: ")
        else:
            print("Please choose a valid option")
            for i, j in enumerate(menus):
                print(f"{i+1} {j}")
            userinput=get_digit("\n choose one of them: ")            







def get_digit(prompt):
    result=input(prompt)
    while not result.isdigit():
        print("Please enter a digit number")
        result=input(prompt)
    result=int(result)
    return result 
def get_user(ursername):
    name=input(ursername)
    print(f"\nWelcome {name}")
    return name
main()    





