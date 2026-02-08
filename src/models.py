from typing import Optional


class Product:
    """Класс, представляющий продукт."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError("Сложение возможно только между продуктами одного типа")
        return self.quantity * self.price + other.quantity * other.price

    @classmethod
    def new_product(cls, product_info: dict, products: Optional[list] = None):
        """Класс-метод для создания нового продукта из словаря."""
        name = product_info.get("name")
        description = product_info.get("description")
        price = product_info.get("price")
        quantity = product_info.get("quantity")

        if products:
            for product in products:
                if product.name == name:
                    quantity += product.quantity
                    price = max(price, product.price)

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Свойство для получения цены продукта."""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для установки новой цены продукта с проверкой на отрицательное значение."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.price:
            print("Вы уверены, что хотите снизить цену? y/n")
            user_answer = input().lower()
            if user_answer == "y":
                self.__price = new_price
        else:
            self.__price = new_price


class Category:
    """Класс, представляющий категорию продуктов."""

    categories_amount = 0
    products_amount = 0

    def __init__(self, name: str, description: str, products: Optional[list] = None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.categories_amount += 1
        Category.products_amount += sum([product.quantity for product in self.__products])

    def __str__(self) -> str:
        return f"{self.name}, количество: {self.products_amount} шт."

    def add_product(self, product: Product):
        """Метод для добавления продукта в категорию."""
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.products_amount += product.quantity

    @property
    def products(self) -> str:
        """Свойство для получения продуктов в категории в виде строки."""
        products = ""
        for product in self.__products:
            products += str(product) + "\n"
        return products

    @property
    def products_list(self) -> list:
        """Свойство для получения списка продуктов в категории."""
        return self.__products


class CategoryIterator:
    """Итератор для перебора продуктов в категории."""

    def __init__(self, category: Category):
        self.category = category
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products_list) - 1:
            self.index += 1
            return self.category.products_list[self.index]
        else:
            raise StopIteration


class Smartphone(Product):
    """Класс, представляющий смартфон, наследуется от класса Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс, представляющий газонную траву, наследуется от класса Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
