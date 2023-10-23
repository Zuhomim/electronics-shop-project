"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item, InstantiateCSVError
import pytest


@pytest.fixture
def smartphone():
    """Возвращает экземпляр класса Смартфон с ценой 10000 и кол-вом 20"""
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def notebook():
    """Возвращает экземпляр класса Ноутбук с ценой 20000 и кол-вом 5"""

    return Item("Ноутбук", 20000, 5)


def test__item_all(smartphone, notebook):
    """Тестируем атрибут хранения созданных экземпляров класса Item"""
    item1 = smartphone
    item2 = notebook
    assert Item.all == [item1, item2]


def test__calculate_total_price(smartphone, notebook):
    """Тестируем метод вычисления суммы всех товаров отдельного экземпляра"""

    assert smartphone.calculate_total_price() == 200000
    assert notebook.calculate_total_price() == 100000


def test__apply_discount(smartphone, notebook):
    """Тестируем метод применения скидки экземпляров класса с разным значением уровня цен"""

    # применяем скидку для экземпляра (класса Item) "ноутбук" (pay_rate = 1, скидка 0%)
    notebook.apply_discount()
    # устанавливаем новый уровень цен (скидка 20%)
    Item.pay_rate = 0.8
    # применяем скидку для экземпляра "смартфон"
    smartphone.apply_discount()

    assert smartphone.price == 8000.0
    assert notebook.price == 20000


def test__item_repr(smartphone, notebook):
    """Тестируем метод repr для каждого экземпляра класса Item"""

    assert smartphone.__repr__() == f"Item('{smartphone.name}', {smartphone.price}, {smartphone.quantity})"
    assert notebook.__repr__() == f"Item('{notebook.name}', {notebook.price}, {notebook.quantity})"


def test__item_name(smartphone):
    """Тестируем сеттер установки значения атрибута name"""

    item1 = smartphone
    item1.name = 'Тестировщик'
    assert smartphone.name == 'Тестировщи'

    item1.name = 'Тест'
    assert smartphone.name == 'Тест'


def test__string_to_number():
    """Тестируем метод конвертации строки в число"""

    assert Item.string_to_number("10.5") == 10
    with pytest.raises(ValueError):
        Item.string_to_number("abc")
    assert Item.string_to_number(10) == print('Данная запись не является числом-строкой')


def test__instantiate_from_csv():
    """Тестируем создание экземпляров класса Item из item.csv и запись в Item.all"""

    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[1].name == 'Ноутбук'
    assert Item.all[2].name == 'Кабель'
    assert Item.all[3].name == 'Мышка'
    assert Item.all[4].name == 'Клавиатура'
    assert Item.all[0].price == 100.0
    assert Item.all[1].price == 1000.0
    assert Item.all[2].price == 10.0
    assert Item.all[3].price == 50.0
    assert Item.all[4].price == 75.0
    assert Item.all[0].quantity == 1
    assert Item.all[1].quantity == 3
    assert Item.all[2].quantity == 5
    assert Item.all[3].quantity == 5
    assert Item.all[4].quantity == 5


def test__item_str(smartphone, notebook):
    """Тестируем магический метод str"""

    item1 = smartphone
    item2 = notebook

    assert item1.__str__() == 'Смартфон'
    assert print(item2) == print('Ноутбук')


def test__item_add(smartphone, notebook):
    """Тестируем сложение объектов Item, а также ошибку при сложении с объектом, не относящимся к классу Item"""

    item1 = smartphone
    item2 = notebook
    assert item1 + item2 == 25

    with pytest.raises(ValueError):
        b = item1 + 10


def test__instantiate_from_csv_error():
    """Тестируем появление исключений для метода instantiate_from_csv:
    пользовательского класса InstantiateCSVError, стандартного FileNotFoundError"""

    instance_error = InstantiateCSVError()

    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('items.csv')

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('src/test_items.csv')

    assert instance_error.__str__() == "Файл items.csv поврежден"
