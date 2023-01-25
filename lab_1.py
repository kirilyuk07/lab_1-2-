import doctest


class Concrete:
    def __init__(self, binder_mass: float, aggregate_mass: float, water_mass: float):
        """
        Создание и подготовка к работе объекта "Бетон"

        :param binder_mass: Масса вяжущего вещества в кг
        :param aggregate_mass: Масса заполнителей в кг
        :param water_mass: Масса воды в кг

        Примеры:
        >>> concrete = Concrete(5, 30, 2.5)  # инициализация экземпляра класса
        """
        if not isinstance(binder_mass, (int, float)):
            raise TypeError("Масса вяжущего должна быть типа int или float")
        if binder_mass <= 0:
            raise ValueError("Масса вяжущего должна быть положительным числом")
        self.binder_mass = binder_mass

        if not isinstance(aggregate_mass, (int, float)):
            raise TypeError("Масса заполнителей должна быть типа int или float")
        if aggregate_mass <= 0:
            raise ValueError("Масса заполнителей должна быть положительным числом")
        self.aggregate_mass = aggregate_mass

        if not isinstance(water_mass, (int, float)):
            raise TypeError("Масса воды должна быть типа int или float")
        if water_mass <= 0:
            raise ValueError("Масса воды должна быть положительным числом")
        self.water_mass = water_mass

    def is_get_concrete(self) -> bool:
        """
        Функция которая проверяет примняются ли все ли составляющие бетона

        Примеры:
        >>> concrete = Concrete(5, 30, 2.5)
        >>> concrete.is_get_concrete()
        """
        ...

    def remove_aggregate_from_concrete(self, estimate_concrete: float) -> None:
        """
        Функция, позволяющая уменьшить массу заполнителя в бетоне

        :param estimate_water: Масса, на которую нужно уменьшить текущую массу заполнителя
        :raise ValueError: Если извлекаемая масса заполнителя превышает текущую массу заполнителя в бетонной смеси,
        то возвращается ошибка.

        :return: Значение реально извлекаемой массы

        Примеры:
        >>> concrete = Concrete(5, 30, 2.5)
        >>> concrete.remove_aggregate_from_concrete(5)
        """
        ...

    def full_concrete_mass(self, capacity_mass: float) -> None:
        """
        Функция, подсчитывающая массу бетонной смеси с массой емкости

        :return: Масса бетонной смеси с емкостью

        Примеры:
        >>> concrete = Concrete(5, 30, 2.5)
        >>> concrete.full_concrete_mass(7)
        """
        ...


class Box:
    def __init__(self, length: float, width: float,  price: int):
        """
        Создание и подготовка к работе объекта "Коробка"

        :param length: Длина основания коробки в см
        :param width: Ширина основания коробки в см
        :param price: Стоимость данного типоразмера коробки в рублях

        Примеры:
        >>> box = Box(25, 10, 200)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина основания коробки должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина основания коробки должна быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина основания коробки должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина основания коробки должна быть положительным числом")
        self.width = width

        if not isinstance(price, int):
            raise TypeError("Стоимость коробки должна быть типа int")
        if price <= 0:
            raise ValueError("Стоимость коробки должна быть положительным числом")
        self.price = price

    def is_get_inform(self) -> bool:
        """
        Функция которая проверяет имеется ли вся необходимая информация для продажи коробки

        Примеры:
        >>> box = Box(25, 10, 200)
        >>> box.is_get_inform()
        """
        ...

    def volume(self, height: float) -> None:
        """
        Функция, подсчитывающая объем коробки заданного типоразмера

        :param height: Высота коробки в см

        :return: Объем коробки заданного типоразмера

        Примеры:
        >>> box = Box(25, 10, 200)
        >>> box.volume(10)
        """
        if not isinstance(height, int):
            raise TypeError("Объем коробки должен быть типа int")
        if height <= 0:
            raise ValueError("Объем коробки должен быть положительным числом")
        ...


class Bulldozer:
    def __init__(self, name: str, application: str, price: float):
        """
        Создание и подготовка к работе объекта "Бульдозер"

        :param name: Наименование бульдозера
        :param application: Бульдозер по типу назначения
        :param price: Стоимость данного бульдозера в млн рублей

        Примеры:
        >>> box = Box("komatsu", "особый", 5.25)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Наименование бульдозера должно быть типа str")
        self.name = name

        if not isinstance(application, str):
            raise TypeError("Тип назначения бульдозера должен быть типа str")
        self.application = application

        if not isinstance(price, (int, float)):
            raise TypeError("Стоимость бульдозера должна быть типа int или float")
        if price <= 0:
            raise ValueError("Стоимость бултдозера должна быть положительным числом")
        self.price = price

    def is_get_inform(self) -> bool:
        """
        Функция которая проверяет имеется ли вся необходимая информация для продажи бульдозера

        Примеры:
        >>> bulldozer = Bulldozer("komatsu", "особый", 5.25)
        >>> bulldozer.is_get_inform()
        """
        ...

    def increase_price_of_bulldozer(self, price_increase: float) -> None:
        """
        Функция, позволяющая увеличить стоимость бултдозера

        :param price_increase: Прирост цены в млн рублей

        Примеры:
        >>> bulldozer = Bulldozer("D65", "Special", 5.25)
        >>> bulldozer.increase_price_of_bulldozer(0.7)
        """
        if not isinstance(price_increase, float):
            raise TypeError("Стоимость коробки должна быть типа int или float")
        if price_increase <= 0:
            raise ValueError("Стоимость коробки должна быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
# Пустая строка