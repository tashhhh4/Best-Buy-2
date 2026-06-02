""" Best Buy 2 - main.py """

import products
import store

# Setup initial store and products
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

best_buy = store.Store(product_list)


# Console helper functions

def print_divider():
    """ Prints a divider to help visually space the UI. """
    print("------")

def print_deco_divider():
    """ Prints a classier divider. """
    print("********")

def print_title():
    """ Prints the main title/header of the program. """
    print("   Store Menu")
    print("   ----------")

def print_order_error_header():
    """ Used when reporting an unsuccessful order to the user. """
    print("XXXXX Order unsuccessful XXXXX")


def print_products(store):
    """ Prints a numbered list of the products in the store. """
    print_divider()
    products = store.get_all_products()
    if not products:
        print("Store inventory is empty!")
    else:
        for i, product in enumerate(products):
            print(f"{i + 1}. ", end="")
            product.show()
    print_divider()


# Menu functions

def list_products(store):
    """ Lists the products. """
    print_products(store)


def show_product_count(store):
    """ Shows the total number of items in the store. """
    num_items = store.get_total_quantity()
    print(f"Total of {num_items} items in the store")


def make_order(store):
    """ Interacts with the user to place purchase orders on products in the store. """
    print_products(store)
    print(("Enter the product numbers and quantities for your desired order."
          " To finish, enter blank text for both prompts."))

    # Product order loop
    orders = []
    error_message = "Error adding product!"

    while True:
        product_number = input("Enter product number: ")
        product_quantity = input("Enter product quantity: ")

        # quit condition
        if product_number == "" and product_quantity == "":
            break

        # add order
        try:
            product_number = int(product_number)
            product_quantity = int(product_quantity)

            if product_number < 1:
                raise IndexError

            if product_quantity < 1:
                raise ValueError

            product = store.get_all_products()[product_number - 1]

            orders.append((product, product_quantity))

        except ValueError:
            print(error_message)

        except IndexError:
            print(error_message)

        finally:
            print()

    if orders:
        try:
            price = store.order(orders)
            print_deco_divider()
            print(f"Order made! Total payment: ${round(price)}")

        except products.ProductShortageError as e:
            print_order_error_header()
            print(e)

        except products.ProductLimitError as e:
            print_order_error_header()
            print(e)


def start(store):
    """ Displays a console menu to the user and allows
    interaction with the store. """

    # Menu choices
    choices = [
        ("List all products in the store", list_products),
        ("Show total amount in store", show_product_count),
        ("Make an order", make_order),
        ("Quit",),
    ]

    # Menu Main Loop
    while True:
        print()
        print_title()
        for i, choice in enumerate(choices):
            print(f"{i + 1}. {choice[0]}")

        try:
            user_choice = int(input("Please enter a number: ").strip())

            if user_choice == len(choices): # Quit signal received
                break

            if not 1 <= user_choice <= len(choices):
                print("Invalid choice! Please try again.")
                continue

            choices[user_choice - 1][1](store)

        except ValueError:
            print("Invalid choice! Please try again.")
            continue


if __name__ == "__main__":
    start(best_buy)
