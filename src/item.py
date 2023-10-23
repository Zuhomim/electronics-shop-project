import csv


class InstantiateCSVError(Exception):
    """Класс обнаружения исключения для метода instantiate_from_csv"""

    def __init__(self, *args):
        self.message = args if args else "Файл items.csv поврежден"

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    @property
    def name(self):
        """геттер атрибута name"""

        return self.__name

    @name.setter
    def name(self, name):
        """сеттер атрибута name"""

        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, csv_path: str):
        """Метод создания экземпляров класса из файла items.csv"""

        cls.all.clear()
        try:
            with open(csv_path, 'rt', newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if not row['name'] or not row['price'] or not row['quantity']:
                        raise InstantiateCSVError()
                    else:
                        cls(str(row['name']), float(row["price"]), int(row["quantity"]))
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл items.csv')
            # print(f'{e.__class__.__name__}: Отсутствует файл items.csv')

    @staticmethod
    def string_to_number(string_num):
        """Возвращает целое число из строки"""

        if isinstance(string_num, str):
            return int(float(string_num))
        else:
            print('Данная запись не является числом-строкой')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """

        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price *= self.pay_rate

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError('Складывать можно только объекты Item и дочерние от них')
