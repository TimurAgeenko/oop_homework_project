from src.data_processor import get_classes_from_data


def test_get_classes_from_data():
    categories = get_classes_from_data("./data/products.json")

    assert len(categories) == 2

    assert categories[0].name == "Смартфоны"
    assert (
        categories[0].description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert categories[0].products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )

    assert categories[1].name == "Телевизоры"
    assert (
        categories[1].description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert categories[1].products == "55 QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"
