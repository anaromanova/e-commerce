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


def test_categories_property(category_1, category_2):
    assert category_1.add_product == 'Samsung Galaxy C23 Ultra, 180000.0 руб.Остаток: 5 шт.'
    assert category_2.add_product == '55" QLED 4K, 123000.0 руб.Остаток: 7 шт.'


def test_categories_setter(category_1, product_1):
    assert len(category_1.products) == 1
    category_1.add_product = product_1
    assert len(category_1.products) == 2

