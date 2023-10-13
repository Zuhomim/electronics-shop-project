import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def iphone():
    """возвращает экземпляр класса Phone: iPhone с ценой 120000, кол-вом 5 и кол-вом сим-карт 2"""

    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def smartphone():
    """возвращает экземпляр класса Phone: Смартфон с ценой 10000 и кол-вом 20"""

    return Item("Смартфон", 10000, 20)


def test__init():
    """тестируем инициализацию класса Phone"""

    with pytest.raises(ValueError):
        phone1 = Phone("iPhone 14", 120_000, 5, 0)


def test__phone_number_of_sim(iphone):
    """тестируем сеттер атрибута number_of_sim класса Phone (number_of_sim: int > 0 - иначе ValueError)"""

    phone1 = iphone
    iphone.number_of_sim = 2

    assert phone1.number_of_sim == 2

    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
        phone1.number_of_sim = 'abc'


def test__addition(smartphone, iphone):
    """тестируем сложение объектов класса Item и дочернего класса (Phone) по атрибуту quantity"""

    item1 = smartphone
    phone1 = iphone

    assert item1 + phone1 == 25


def test__repr(iphone):
    """тестурем метод repr класса Phone"""

    iphone1 = iphone

    assert iphone1.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"
