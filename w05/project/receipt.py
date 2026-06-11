
import csv
from datetime import datetime


def main():
    
    try:
        
        products_dict = read_dictionary("w05/project/products.csv", 0)

        print("Inkom Emporium")
        

        total_items = 0
        subtotal = 0

        with open("w05/project/request.csv", "rt") as request:
            reader = csv.reader(request)
            next(reader) 
            for row in reader:
                product_id = row[0]
                quantity = int(row[1])

                try:
                   
                    product = products_dict[product_id]
                    name = product[1]
                    price = float(product[2])

                    print(f"{name}: {quantity} @ {price:.2f}")
                  
                    total_items += quantity
                    subtotal += quantity * price
                
                except KeyError:
                    print(f"Error: unknown product ID in the request.csv file")
                    print(f"'{product_id}'")
                    raise

        tax = subtotal * 0.06
        total = subtotal + tax
        

        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {tax:.2f}")
        print(f"Total: {total:.2f}")
        
        print(f"Thank you for shopping at the Inkom Emporium.")
        
        print(f"{datetime.now():%a %b %d %H:%M:%S %Y}")
    
    except FileNotFoundError as e:
        print(f"Error: missing file")
        print(f"{e}")
    
    except PermissionError as e:
        print(f"Error: permission denied")
        print(f"{e}")



def read_dictionary(filename, key_column_index):
    products_dict = {}
    with open(filename, "rt") as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            key = row[key_column_index]
            products_dict[key] = row
    return products_dict        


if __name__ == "__main__":
    main()