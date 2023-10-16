import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    """Возвращает экземпляр класса Keyboard 'Dark Project KD87A' с ценой 9600 и кол-вом 5"""

    return Keyboard('Dark Project KD87A', 9600, 5)


def test__init(keyboard):
    """Тестируем создание экземпляра класса Keyboard с доп атрибутом language (по умолчанию EN)"""

    keyboard1 = keyboard

    assert keyboard1.language == "EN"
    assert str(keyboard1) == "Dark Project KD87A"


def test__change_lang(keyboard):
    """Тестируем метод изменения атрибута language и невозможность изменения атрибута напрямую (присвоением значения)"""

    keyboard1 = keyboard

    keyboard1.change_lang()
    assert keyboard1.language == "RU"

    keyboard1.change_lang()
    assert keyboard1.language == "EN"

    with pytest.raises(AttributeError):
        keyboard1.language = "RU"
