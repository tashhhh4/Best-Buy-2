import pytest
from products import Product, ProductShortageError

def test_creating_prod():
    thing1 = Product("Mousepad", 10, 100)
    assert thing1.name == "Mousepad"
    assert thing1.price == 10
    assert thing1.get_quantity() == thing1.quantity
    assert thing1.is_active()


def test_creating_prod_invalid_details():
    with pytest.raises(ValueError):
        thing2 = Product("Nintendo Switch", 300, -1)

    with pytest.raises(ValueError):
        thing3 = Product("", 5, 100)

    with pytest.raises(ValueError):
        thing4 = Product("Gameboy Advanced", -50, 200)


def test_prod_becomes_inactive():
    thing5 = Product("Playstation 2", 260, 300)
    thing5.set_quantity(0)
    assert thing5.get_quantity() == thing5.quantity == 0
    assert thing5.is_active() is False
    thing5.set_quantity(1)
    assert thing5.is_active() is True
    

def test_buy_modifies_quantity():
    thing6 = Product("Xbox 360", 500, 100)
    thing6.buy(1)
    assert thing6.get_quantity() == 99


def test_buy_too_much():
    thing7 = Product("Steam Deck", 400, 80)
    thing7.buy(80)
    assert thing7.is_active() is False
    with pytest.raises(ProductShortageError):
        thing7.buy(1)