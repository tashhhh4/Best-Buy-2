""" Best Buy 2 - promotions.py """

import abc

class Promotion(abc.ABC):
    """ Abstract base class for promotions. """

    def __init__(self, name):
        """ Creates a Promotion with a 'name' property.
        
            Args:
                name :: str :: A short (<= 5 words), enticing description of this
                                  promotion and how it works.
        """
        self.name = name

    def __str__(self):
        """ Uses the 'name' property to represent this promotion in product listings. """
        return self.name

    @abc.abstractmethod
    def apply_promotion(self, product, quantity):
        """ Applies the discount based on the product's base price, the quantity
        ordered, and the internal rules of the particular Promotion.
        
            Returns:
                final_price :: The price of the given quantity of items after
                               applying the discount.
        """    


class PercentDiscount(Promotion):
    """ Applies a percentage discount to the item price. """

    def __init__(self, message, percent):
        self.percent = percent
        super().__init__(message)

    def apply_promotion(self, product, quantity):
        final_price = product.price * quantity
        return final_price


class SecondHalfPrice(Promotion):
    """ For every two items (of the same product) that are purchased,
    the second one gets half off. """

    def apply_promotion(self, product, quantity):
        final_price = product.price * quantity
        return final_price


class ThirdOneFree(Promotion):
    """ For every three items (of the same product) that are purchased,
    the third one is free! """

    def apply_promotion(self, product, quantity):
        final_price = product.price * quantity
        return final_price