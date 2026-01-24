from typing import Optional


class Product:
    """Класс, представляющий продукт."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс, представляющий категорию продуктов."""

    categories_amount = 0
    products_amount = 0

    def __init__(self, name: str, description: str, products: Optional[list] = None):
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.categories_amount += 1
        Category.products_amount += sum([product.quantity for product in self.products])
