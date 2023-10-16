from src.item import Item


class KeyboardMixin:
    """Миксин для класса Keyboard с доп атрибутом language и методом изменения данного атрибута"""
    __language = "EN"

    def change_lang(self):
        """Метод изменения атрибута language EN - RU"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

    @property
    def language(self):
        """Геттер атрибута language"""

        return self.__language


class Keyboard(Item, KeyboardMixin):
    """Класс, наследуемый от Item и KeyboardMixin (доп.атрибут language: по умолчанию EN)"""

    language = KeyboardMixin.language

    def __init__(self, name, price, quantity) -> None:
        super().__init__(name, price, quantity)
        self.__name = name

    def __str__(self):
        return f'{self.__name}'
