import pytest

from src.models import CategoryIterator, Product, Smartphone, Order, Category


def test_product_initialization(product):
    assert product.name == "Laptop"
    assert product.description == "A high-end gaming laptop"
    assert product.price == 50000.00
    assert product.quantity == 10

def test_product_quantity_error():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Laptop", "A high-end gaming laptop", 50000.00, 0)


def test_new_product():
    product_info = {"name": "Smartphone", "description": "Latest model smartphone", "price": 70000.00, "quantity": 15}
    new_product = Product.new_product(product_info)
    assert new_product.name == "Smartphone"
    assert new_product.description == "Latest model smartphone"
    assert new_product.price == 70000.00
    assert new_product.quantity == 15

    products = [
        Product("Laptop", "A high-end gaming laptop", 50000.00, 10),
        Product("Mouse", "Wireless mouse", 3000.00, 50),
    ]

    product_info = {"name": "Laptop", "description": "A high-end gaming laptop", "price": 70000.00, "quantity": 15}
    new_product = Product.new_product(product_info, products)
    assert new_product.name == "Laptop"
    assert new_product.description == "A high-end gaming laptop"
    assert new_product.price == 70000.00
    assert new_product.quantity == 25


def test_price_setter(product, capsys):
    assert product.price == 50000.00
    product.price = 60000.00
    assert product.price == 60000.00

    product.price = -100.00
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_str_product(product):
    assert str(product) == "Laptop, 50000.0 руб. Остаток: 10 шт."


def test_add_product(product):
    another_product = Product("Mouse", "Wireless mouse", 3000.00, 50)
    total_price = product + another_product
    assert total_price == 650000.0


def test_add_product_invalid_type(smartphone, grass):
    with pytest.raises(TypeError) as exc_info:
        smartphone + grass

    assert str(exc_info.value) == "Сложение возможно только между продуктами одного типа"


def test_mixin_logger(capsys):
    Product("Laptop", "A high-end gaming laptop", 50000.00, 10)
    captured = capsys.readouterr()
    assert captured.out == "Product('Laptop', 'A high-end gaming laptop', 50000.0, 10)\n"

    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    captured = capsys.readouterr()
    assert captured.out == "Smartphone('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)\n"


def test_category_initialization(category):
    assert category.name == "Electronics"
    assert category.description == "Electronic gadgets and devices"
    assert category.products == "Laptop, 50000.0 руб. Остаток: 10 шт.\nMouse, 3000.0 руб. Остаток: 50 шт.\n"


def test_products_amount(category):
    assert category.products_amount == 60


def test_categories_amount(category):
    assert category.categories_amount == 1


def test_add_product_category(category):
    new_product = Product("Keyboard", "Mechanical keyboard", 7000.00, 20)
    category.add_product(new_product)
    assert category.products == (
        "Laptop, 50000.0 руб. Остаток: 10 шт.\n"
        "Mouse, 3000.0 руб. Остаток: 50 шт.\n"
        "Keyboard, 7000.0 руб. Остаток: 20 шт.\n"
    )
    assert category.products_amount == 80


def test_add_product_category_invalid_type(category):
    with pytest.raises(TypeError) as exc_info:
        category.add_product("Not a product")

    assert str(exc_info.value) == "В категорию можно добавлять только объекты класса Product или его наследников"


def test_str_category(category):
    assert str(category) == "Electronics, количество: 60 шт."


def test_products_list(category):
    products_list = category.products_list
    assert len(products_list) == 2
    assert products_list[0].name == "Laptop"
    assert products_list[1].name == "Mouse"


def test_middle_price(category):
    average_price = category.middle_price()
    assert average_price == 10833.33


def test_middle_price_empty_category():
    empty_category = Category("Empty", "No products")
    average_price = empty_category.middle_price()
    assert average_price == 0.0


def test_category_iterator(category):
    category_iterator = CategoryIterator(category)
    product_1 = next(category_iterator)
    assert product_1.name == "Laptop"
    product_2 = next(category_iterator)
    assert product_2.name == "Mouse"


def test_smartphone_initialization(smartphone):
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawn_grass_initialization(grass):
    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава для газона"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_order_initialization(product):
    order = Order(product, 2)
    assert order.product == product
    assert order.quantity == 2
    assert order.total_price == 100000.0
    assert str(order) == "Заказ: Laptop, количество: 2 шт., общая стоимость: 100000.0 руб."
