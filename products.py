""" Best Buy - products.py """

class ProductShortageError(Exception):
    """ Raised when attempting to decrease a product's stock below zero. """


class Product:
    """ A product in the store inventory. """

    def __init__(self, name, price, quantity):
        """ Sets the data and initial quantity the product.
        A product is considered "active" if quantity > 0.
        All fields required.
        """
        if not name:
            raise ValueError("Expected a value for property 'name' in new 'Product'.")

        self.name = name

        self.price = float(price)
        if price < 0:
            raise ValueError("Property 'price' can't be negative in class 'Product'.")

        self.set_quantity(quantity)

        self.active = quantity > 0

    def get_quantity(self):
        """ Returns the current quantity of this product. """
        return self.quantity

    def set_quantity(self, quantity):
        """ Updates the quantity of this product. """
        quantity = int(quantity)
        if quantity < 0:
            raise ValueError(("Tried to set property 'quantity' to a negative value"
                              " in setter function 'set_quantity' in class Product."
            ))

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """ Reports if this product is active. """
        return self.active

    def activate(self):
        """ Sets this product's status to active (`True`). """
        self.active = True

    def deactivate(self):
        """ Sets this product's status to inactive (`False`). """
        self.active = False

    def show(self):
        """ Prints an string representation of the product containing all of its basic info. """
        print(f"{self.name}, Price: {round(self.price)}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """ 'Buys' a product. Returns the total price given the desired quantity,
        and deducts the product from the store's total inventory. """
        if self.quantity <= 0:
            raise ProductShortageError(f"Product '{self.name}' is out of stock!")
        if self.quantity < quantity:
            raise ProductShortageError((f"Cannot buy {quantity} of product '{self.name}' "
                                       f" with only {self.quantity} left in stock!"
            ))

        self.set_quantity(self.quantity - quantity)
        return quantity * self.price


# Run tests on the Product class
if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))

    print(mac.is_active())
    assert mac.is_active() is False

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

    try:
        print(mac.buy(5))
    except ProductShortageError as e:
        print(e)

    try:
        print(bose.buy(40000))
    except ProductShortageError as e:
        print(e)
