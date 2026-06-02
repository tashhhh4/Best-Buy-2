""" Best Buy 2 - promotions.py """

import abc

class Promotion(abc.ABC):
    """ Abstract base class for promotions. """


class PercentDiscount(Promotion):
    """ Applies a percentage discount to the item price. """


class SecondHalfPrice(Promotion):
    """ For every two items (of the same product) that are purchased,
    the second one gets half off. """


class ThirdOneFree(Promotion):
    """ For every three items (of the same product) that are purchased,
    the third one is free! """