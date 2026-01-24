from src.data_processor import get_classes_from_data


def test_get_classes_from_data():
    categories = get_classes_from_data("./data/products.json")

    assert len(categories) == 2

    assert categories[0].name == "Смартфоны"
    assert (
        categories[0].description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert len(categories[0].products) == 3
    assert categories[0].products[0].name == "Samsung Galaxy C23 Ultra"
    assert categories[0].products[1].name == "Iphone 15"

    assert categories[1].name == "Телевизоры"
    assert (
        categories[1].description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(categories[1].products) == 1
    assert categories[1].products[0].name == "55 QLED 4K"
