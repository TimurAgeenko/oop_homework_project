import pytest

from src.models import Category, Product


@pytest.fixture
def product():
    return Product("Laptop", "A high-end gaming laptop", 50000.00, 10)


@pytest.fixture
def category():
    Category.categories_amount = 0
    Category.products_amount = 0

    products = [
        Product("Laptop", "A high-end gaming laptop", 50000.00, 10),
        Product("Mouse", "Wireless mouse", 3000.00, 50),
    ]
    return Category("Electronics", "Electronic gadgets and devices", products)
