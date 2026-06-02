""" Best Buy - store.py """

import products


class Store:
    """ The store tracks a list of products that belong to it. """

    def __init__(self, products):
        """ Initializes the Store with an initial Product list.

            Args:
                products :: List[products.Product]
        """
        self.products = products

    def add_product(self, product):
        """ Adds a Product to the Store. """
        self.products.append(product)

    def remove_product(self, product):
        """ Removes the Product from the Store. """
        self.products.remove(product)

    def get_total_quantity(self):
        """ Returns a count of the total number of items (of all Products) in the Store. """
        count = 0
        for product in self.products:
            count += product.get_quantity()
        return count

    def get_all_products(self):
        """ Returns a list of all Products (only active) in the Store. """
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list):
        """ Processes a purchase order for the Store.

            Returns:
                total :: The total price of the order

            Args:
                shopping_list :: tuple(products.Product, quantity)
        """
        total = 0
        for product, quantity in shopping_list:
            cost = product.buy(quantity)
            total += cost
        return total


# Tests
if __name__ == "__main__":
    try:
        # Create Store
        my_store = Store([])
        assert len(my_store.get_all_products()) == 0

        # Add Products
        p1 = products.Product("Product 1", 10.99, 10)
        p2 = products.Product("Product 2", 25.99, 5)

        my_store.add_product(p1)
        my_store.add_product(p2)

        # Get all Products
        assert len(my_store.get_all_products()) == 2
        assert p2 in my_store.get_all_products()

        # Remove Products
        my_store.remove_product(p2)

        # Test buying function
        price = my_store.order([(p1, 2)])
        assert price == 10.99 * 2

        # Count total quantity
        assert my_store.get_total_quantity() == 8

        # Create new products
        bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
        mac = products.Product("MacBook Air M2", price=1450, quantity=100)

        # Initialize store with products
        best_buy = Store([bose, mac])
        assert len(best_buy.get_all_products()) == 2
        assert best_buy.get_all_products()[0] is bose

        # Add another product
        pixel = products.Product("Google Pixel 7", price=500, quantity=250)
        best_buy.add_product(pixel)

        # Test correct quantity counting
        assert (best_buy.get_total_quantity() ==
                bose.get_quantity() + mac.get_quantity() + pixel.get_quantity()
        )

        # Test deactivated product
        pixel.deactivate()

        assert pixel not in best_buy.get_all_products()

        # Test order
        price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
        assert price == bose.price * 15 + mac.price * 30
        assert bose.get_quantity() == 500 - 5 - 10

        # Test one more set of usage statements (note: best_buy variable reassigned)
        product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

        best_buy = Store(product_list)
        products = best_buy.get_all_products()
        assert best_buy.get_total_quantity() == 100 + 500 + 250
        assert (best_buy.order([(products[0], 1), (products[1], 2)]) ==
                products[0].price * 1 + products[1].price * 2
        )

        print("All tests passed.")

    except Exception as e:
        print("Test failed...")
        print(e)
