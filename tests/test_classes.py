from src.classes import Product
from unittest.mock import patch
import pytest


def test_products_init(product_1, product_2):
    assert product_1.name == "55\" QLED 4K"
    assert product_1.description == "Фоновая подсветка"
    assert product_1.price == 123000.0
    assert product_1.quantity == 7
    assert product_2.name == "Samsung Galaxy C23 Ultra"
    assert product_2.description == "256GB, Серый цвет, 200MP камера"
    assert product_2.price == 180000.0
    assert product_2.quantity == 5


def test_products_create():
    product = Product('1234', '1234 телефон', 12000, 3)
    product.name = '1234'
    product.description = '1234 телефон'
    product.price = 12000
    product.quantity = 3


@patch("src.classes.input")
def test_products_update(mock_input, product_1):
    mock_input.side_effect = ["y"]
    assert product_1.price == 123000.0
    product_1.price = 125000.0
    assert product_1.price == 125000.0


def test_categories_init(category_1, category_2):
    assert category_1.name == 'Смартфоны'
    assert category_1.description == 'Смартфоны,\
 как средство не только коммуникации,\
 но и получение дополнительных функций для удобства жизни'
    assert category_2.name == 'Телевизоры'
    assert category_2.description == 'Современный телевизор,\
 который позволяет наслаждаться просмотром,\
 станет вашим другом и помощником'
    assert category_1.category_count == 2
    assert category_2.category_count == 2
    assert category_1.product_count == 2
    assert category_2.product_count == 2
    assert len(category_1.products) == 1
    assert len(category_2.products) == 1


def test_categories_property(category_1, product_1):
    assert category_1.product_count == 3
    category_1.add_product(product_1)
    assert category_1.product_count == 4


def test_categories_setter(category_1, product_1):
    assert len(category_1.products) == 1
    category_1.add_product(product_1)
    assert len(category_1.products) == 2


def test_str_products(product_1):
    assert str(product_1) == "55\" QLED 4K, 123000.0 руб. Остаток: 7 шт."


def test_add_products(product_1, product_2):
    assert product_1 + product_2 == 1761000.0


def test_str_categories(category_1):
    assert str(category_1) == "Смартфоны, количество продуктов: 5 шт."


def test_smartphone_init(smartphone_1, smartphone_2):
    assert smartphone_1.name == "IPhone 15"
    assert smartphone_1.description == "Apple"
    assert smartphone_1.price == 50000
    assert smartphone_1.quantity == 200
    assert smartphone_1.color == 'green'
    assert smartphone_1.memory == 256
    assert smartphone_2.name == "IPhone 14"
    assert smartphone_2.description == "Apple"
    assert smartphone_2.price == 40000
    assert smartphone_2.quantity == 200
    assert smartphone_2.color == 'gold'
    assert smartphone_2.memory == 256


def test_lawngrass_init(lawngrass_1, lawngrass_2):
    assert lawngrass_1.name == "grass"
    assert lawngrass_1.description == "grass from China"
    assert lawngrass_1.price == 800
    assert lawngrass_1.quantity == 100
    assert lawngrass_1.color == 'green'
    assert lawngrass_1.country == 'China'
    assert lawngrass_2.name == "grass"
    assert lawngrass_2.description == "grass from Finland"
    assert lawngrass_2.price == 1800
    assert lawngrass_2.quantity == 200
    assert lawngrass_2.color == 'green'
    assert lawngrass_2.country == 'Finland'


def test_add_products_error(product_1, lawngrass_1):
    with pytest.raises(TypeError):
        result = product_1 + lawngrass_1


def test_categories_setter_error(category_1, category_2):
    with pytest.raises(TypeError):
        category_1.add_product(category_2)
