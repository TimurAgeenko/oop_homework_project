import json

from src.models import Category, Product


def get_classes_from_data(path: str = "../data/products.json") -> list:
    """Функция для создания классов из JSON файла. Возвращает список объектов класса 'Category'."""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []

    for category in data:
        products = []

        for product in category["products"]:
            products.append(
                Product(
                    name=product["name"],
                    description=product["description"],
                    price=product["price"],
                    quantity=product["quantity"],
                )
            )

        category["products"] = products

        categories.append(Category(category["name"], category["description"], category["products"]))

    return categories
