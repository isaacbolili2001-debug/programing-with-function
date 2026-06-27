import csv
import pytest

from online_shopping import add_to_cart, add_to_cart, login, payment, payment, remove_from_cart, sign_up, view_cart

    

def test_get_digital_number_valid(monkeypatch):
    from online_shopping import get_digital_number
    monkeypatch.setattr("builtins.input", lambda _: "123")
    assert get_digital_number("Enter number: ") == 123


def test_get_digital_number_invalid_then_valid(monkeypatch):
    from online_shopping import get_digital_number
    inputs = iter(["abc", "45"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_digital_number("Enter number: ") == 45  


"""def test_username_check_new_user(monkeypatch, tmp_path):
    from online_shopping import username_check
    file = tmp_path / "connexion.csv"

    # create fake CSV
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["username", "password"])
        writer.writerow(["john", "123"])

    monkeypatch.setattr("builtins.input", lambda _: "newuser")

    result = username_check(file)
    assert result == "newuser" 
def test_username_check_existing_user(monkeypatch, tmp_path):
    from online_shopping import username_check
    file = tmp_path / "connexion.csv"

    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["username", "password"])
        writer.writerow(["john", "123"])

    inputs = iter(["john", "newuser"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = username_check(file)
    assert result == "newuser" """



def test_sign_up(tmp_path, monkeypatch):
    from online_shopping import sign_up
    file = tmp_path / "users.csv"

    # Simulate user input
    inputs = iter(["john123", "pass456"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = sign_up(file)

    assert result == True

    # Verify file content
    with open(file, "r") as f:
        rows = list(csv.reader(f))

    assert rows[1] == ["john123", "pass456"]

def test_sign_up_duplicate(tmp_path, monkeypatch):
    file = tmp_path / "users.csv"

    # Create existing user
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["username", "password"])
        writer.writerow(["john123", "pass456"])

    inputs = iter(["john123", "newpass"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = sign_up(file)

    assert result == False


def test_login_success(monkeypatch, tmp_path):
    from online_shopping import login
    file = tmp_path / "connexion.csv"

    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["username", "password"])
        writer.writerow(["john", "123"])

    inputs = iter(["john", "123"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    assert login(file) == True

def test_login_fail(monkeypatch, tmp_path):
    file = tmp_path / "connexion.csv"

    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["username", "password"])
        writer.writerow(["john", "123"])

    inputs = iter(["john", "wrong"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    assert login(file) == False

def show_products_by_category(filename, selected_category):
    from online_shopping import show_products_by_category
    results = []
    with open(filename, "rt") as product:
        reader = csv.reader(product)
        next(reader)
        for row in reader:
            if row[2] == selected_category:
                results.append(row)
    return results

def test_show_products(tmp_path):
    from online_shopping import show_products_by_category
    file = tmp_path / "products.csv"

    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "category", "price", "stock"])
        writer.writerow(["1", "Phone", "Electronics", "500", "10"])
        writer.writerow(["2", "Shirt", "Clothing", "20", "50"])

    result = show_products_by_category(file, "Electronics")

    assert len(result) == 1
    assert result[0][1] == "Phone"



def test_add_to_cart_success(tmp_path):
    from online_shopping import add_to_cart
    product_file = tmp_path / "products.csv"
    cart_file = tmp_path / "cart.csv"

    # Create product file
    with open(product_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "category", "price", "stock"])
        writer.writerow(["P1", "Phone", "Electronics", "500", "10"])

    result = add_to_cart(product_file, cart_file, "P1", 2)

    assert result == True

    # Verify cart content
    with open(cart_file, "r") as f:
        rows = list(csv.reader(f))
        assert rows[0][0] == "P1"
        assert rows[0][3] == "2"    

def test_add_to_cart_not_enough_stock(tmp_path):
    
    product_file = tmp_path / "products.csv"
    cart_file = tmp_path / "cart.csv"

    with open(product_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "category", "price", "stock"])
        writer.writerow(["P1", "Phone", "Electronics", "500", "5"])

    result = add_to_cart(product_file, cart_file, "P1", 10)

    assert result == False

def test_add_to_cart_product_not_found(tmp_path):

    product_file = tmp_path / "products.csv"
    cart_file = tmp_path / "cart.csv"

    with open(product_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "category", "price", "stock"])

    result = add_to_cart(product_file, cart_file, "P99", 1)

    assert result == False



def test_remove_from_cart(tmp_path):
    from online_shopping import remove_from_cart
    cart_file = tmp_path / "cart.csv"

    with open(cart_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["P1", "Phone", "500", "2"])
        writer.writerow(["P2", "Laptop", "1000", "1"])

    remove_from_cart(cart_file, "P1")

    with open(cart_file, "r") as f:
        rows = list(csv.reader(f))

    assert len(rows) == 1
    assert rows[0][0] == "P2"


def test_payment(tmp_path):
    from online_shopping import payment
    file = tmp_path / "cart.csv"

    # Create sample cart
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["P001", "Laptop", "1000", "1"])
        writer.writerow(["P002", "Mouse", "50", "2"])

    # Run payment
    result = payment(file)

    # Check payment success
    assert result == True

    # Verify cart is cleared
    with open(file, "r") as f:
        content = f.read()

    assert content == ""

def test_payment_empty(tmp_path):
    
    file = tmp_path / "cart.csv"

    # Create empty file
    open(file, "w").close()

    result = payment(file)

    assert result == False     