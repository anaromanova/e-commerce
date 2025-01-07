class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб.Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(self) is type(other):
            return "self.price() * self.quantity + other.price() * other.quantity"


    @classmethod
    def new_product(cls, dict_of_product: dict):
        for product in Category.products():
            if dict_of_product['name'] == product.name:
                quantity = dict_of_product["quantity"] + product.quantity
                cls.quantity = quantity
            else:
                cls.quantity = dict_of_product["quantity"]
        for product in Category.products():
            if dict_of_product["name"] == product.name:
                max_price = max(dict_of_product["price"], product.price)
                cls.__price = max_price
        cls.name = dict_of_product["name"]
        cls.description = dict_of_product["description"]
        cls.quantity = dict_of_product["quantity"]
        return Product(cls.name, cls.description, cls.quantity, cls.__price)


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price > 0 and self.__price < new_price:
            print("Цена будет выше предыдущей: Y / N")
            answer = input().lower()
            if answer == "y":
                self.__price = new_price
        elif self.__price > new_price:
            print("Цена будет ниже предыдущей: Y / N")
            answer = input().lower()
            if answer == "y":
                self.__price = new_price


class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        products_sum = 0
        for product in Category.__products:
            products_sum += product.quantity
        return f'{product.name}, количество продуктов: {products_sum} шт.'


    @staticmethod
    def str_category() -> list[str]:
        products_str = []
        for product in Category.__products:
            products_str.append(f'{product.name}, {product.price} руб.Остаток: {product.quantity} шт.\n')
        return products_str

    @staticmethod
    def products():
        return Category.__products

    @staticmethod
    def add_product(new_product: Product):
        Category.__products.append(new_product)
        Category.product_count += 1
