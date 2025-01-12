import json

from src.classes import Product, Category


def reading_json(path: str) -> dict:
    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: dict) -> list:
    categories = []
    for category in data:
        products_list = []
        for product in category["products"]:
            products_list.append(Product(**product))
        category["products"] = products_list
        categories.append(Category(**category))
    return categories
