from src.products import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


    @property
    def add_product(self):
        products_str = ''
        for product in self.__products:
            products_str += f'{product.name}, {product.price} руб.Остаток: {product.quantity} шт.'
        return products_str

    @property
    def products(self):
        return self.__products

    @add_product.setter
    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1



# product1 = Product('1', '1 grgrg', '123', '3')
# product2 = Product('2', '2 grgrg', '124', '5')
#
# category1 = Category('12', '12 rgd', [product1, product2])
#
# product1 = Product('2', '2 grgrg', '124', '5')
#
# print(category1.name)
# print(category1.product_count)


