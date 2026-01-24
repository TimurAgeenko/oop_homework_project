def test_product_initialization(product):
    assert product.name == "Laptop"
    assert product.description == "A high-end gaming laptop"
    assert product.price == 50000.00
    assert product.quantity == 10


def test_category_initialization(category):
    assert category.name == "Electronics"
    assert category.description == "Electronic gadgets and devices"
    assert len(category.products) == 2
    assert category.products[0].name == "Laptop"
    assert category.products[1].name == "Mouse"


def test_products_amount(category):
    assert category.products_amount == 60


def test_categories_amount(category):
    assert category.categories_amount == 1
