import pytest

from src.models import Category, Product, Smartphone, LawnGrass


@pytest.fixture
def product():
    return Product("Laptop", "A high-end gaming laptop", 50000.00, 10)


@pytest.fixture
def smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def category():
    Category.categories_amount = 0
    Category.products_amount = 0

    products = [
        Product("Laptop", "A high-end gaming laptop", 50000.00, 10),
        Product("Mouse", "Wireless mouse", 3000.00, 50),
    ]
    return Category("Electronics", "Electronic gadgets and devices", products)
