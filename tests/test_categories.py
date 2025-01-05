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


def test_products_init(product_1, product_2):
    assert product_1.name == "55\" QLED 4K"
    assert product_1.description == "Фоновая подсветка"
    assert product_1.price == 123000.0
    assert product_1.quantity == 7
    assert product_2.name == "Samsung Galaxy C23 Ultra"
    assert product_2.description == "256GB, Серый цвет, 200MP камера"
    assert product_2.price == 180000.0
    assert product_2.quantity == 5
