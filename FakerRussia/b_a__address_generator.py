import random
from dataclasses import dataclass
from .b_h__base_generator import BaseGenerator
from FakerRussia.b__additional_algorithms.a_a__handle_errors import handle_errors


@dataclass
class _AddressData:
    """
    Суть: Внутренний контейнер данных для хранения состояния генератора адресов. Хранит
    сгенерированные компоненты адреса (регион, город, улица, адрес регистрации, фактический
    адрес, тип жилья) для обеспечения согласованности данных при множественных обращениях к свойствам.
    """
    region: str = None
    city: str = None
    street: str = None
    registration_address: str = None
    actual_address: str = None
    housing_type: str = None


class AddressGenerator(BaseGenerator):
    """
    Суть: Генератор российских адресных данных. Предоставляет функциональность для генерации
    компонентов адреса: регион, город, улица, адрес регистрации, фактический адрес, тип жилья.
    Данные загружаются из JSON-файлов. Поддерживает сброс сгенерированных данных для создания
    нового набора адресных компонентов.
    """

    def __init__(self):
        """
        Суть: Инициализация генератора адресов. Создает экземпляр генератора, инициализирует
        внутреннее хранилище данных _AddressData и загружает адресные данные из JSON-файлов
        (регионы, города, улицы, почтовые индексы, типы жилья) через метод _load_address_data.
        """
        super().__init__()
        self._data = _AddressData()
        self._load_address_data()

    def _load_address_data(self):
        """
        Суть: Загрузка адресных данных из JSON-файлов. Загружает данные о регионах, городах
        и улицах из файла 'a__data/address/regions_cities_streets.json', почтовые индексы из
        файла 'a__data/address/postal_codes.json', типы жилья из файла 'a__data/housing_type/housing_types.json'.
        Сохраняет загруженные данные в атрибуты класса REGIONS_CITIES_STREETS, POSTAL_CODES, HOUSING_TYPES.
        """
        regions_data = self._load_json('a__data/address/regions_cities_streets.json')
        self.REGIONS_CITIES_STREETS = regions_data.get("REGIONS_CITIES_STREETS", {})
        postal_codes_data = self._load_json('a__data/address/postal_codes.json')
        self.POSTAL_CODES = postal_codes_data.get("POSTAL_CODES", {})
        housing_types_data = self._load_json('a__data/housing_type/housing_types.json')
        self.HOUSING_TYPES = housing_types_data.get("HOUSING_TYPES", [])

    def reset(self):
        """
        Суть: Сброс сгенерированных адресных данных. Очищает внутреннее хранилище данных,
        создавая новый экземпляр _AddressData, что позволяет сгенерировать новый набор
        адресных компонентов при последующих обращениях к свойствам.
        """
        self._data = _AddressData()
        return "Адресные данные сброшены"

    @property
    @handle_errors
    def region(self) -> str:
        """
        Суть: Получение названия региона. Возвращает сгенерированное название региона.
        При первом обращении случайным образом выбирает регион из загруженного списка
        REGIONS_CITIES_STREETS. Последующие обращения возвращают сохраненное значение
        из внутреннего хранилища.
        """
        if self._data.region is None:
            self._data.region = random.choice(list(self.REGIONS_CITIES_STREETS.keys()))
        return self._data.region

    @property
    @handle_errors
    def city(self) -> str:
        """
        Суть: Получение названия города. Возвращает сгенерированное название города.
        При первом обращении случайным образом выбирает город из списка городов текущего
        региона (self.region). Последующие обращения возвращают сохраненное значение из
        внутреннего хранилища.
        """
        if self._data.city is None:
            self._data.city = random.choice(list(self.REGIONS_CITIES_STREETS[self.region].keys()))
        return self._data.city

    @property
    @handle_errors
    def street(self) -> str:
        """
        Суть: Получение названия улицы. Возвращает сгенерированное название улицы. При
        первом обращении случайным образом выбирает улицу из списка улиц текущего города
        (self.city). Последующие обращения возвращают сохраненное значение из внутреннего хранилища.
        """
        if self._data.street is None:
            self._data.street = random.choice(self.REGIONS_CITIES_STREETS[self.region][self.city])
        return self._data.street

    @property
    @handle_errors
    def registration_address(self) -> str:
        """
        Суть: Формирование полного адреса регистрации. Создает строку адреса, включающую
        почтовый индекс, регион, город, улицу и номер дома. Номер дома генерируется
        случайно от 1 до 300. С вероятностью 50% добавляет корпус/строение со случайным
        номером от 1 до 50. Использует TYPE_BUILDINGS из базового класса для обозначения
        дома и корпуса. Формат: "индекс, регион - Город город - улица д. номер [корпус номер]".
        """
        if self._data.registration_address is None:
            answer = f"{self.region} - Город {self.city} - {self.street}"
            first_building = self.TYPE_BUILDINGS[0]
            number_first_buildings = random.randint(1, 300)
            postal_code = self.POSTAL_CODES[self.city]
            if random.choice([True, False]):
                second_buildings = self.TYPE_BUILDINGS[1]
                number_second_buildings = random.randint(1, 50)
                text = f"{first_building} {number_first_buildings} {second_buildings} {number_second_buildings}"
                self._data.registration_address = f"{postal_code}, {answer} {text}"
            else:
                text = f"{first_building} {number_first_buildings}"
                self._data.registration_address = f"{postal_code}, {answer} {text}"
        return self._data.registration_address

    @property
    @handle_errors
    def actual_address(self) -> str:
        """
        Суть: Формирование полного фактического адреса. С вероятностью 30% возвращает
        строку "Совпадает с адресом регистрации". В остальных случаях с вероятностью
        50% генерирует адрес в том же городе, но на другой улице (с исключением
        повторения текущей улицы), либо в другом регионе и городе. Номер дома
        генерируется случайно от 1 до 300. Формат: "индекс, регион - Город город - улица д. номер".
        """
        if self._data.actual_address is None:
            if random.random() < 0.3:
                self._data.actual_address = "Совпадает с адресом регистрации"
                return self._data.actual_address
            if random.choice([True, False]):
                other_street = random.choice(self.REGIONS_CITIES_STREETS[self.region][self.city])
                while other_street == self.street and len(self.REGIONS_CITIES_STREETS[self.region][self.city]) > 1:
                    other_street = random.choice(self.REGIONS_CITIES_STREETS[self.region][self.city])
                other_postal_code = self.POSTAL_CODES[self.city]
                building = random.randint(1, 300)
                self._data.actual_address = f"{other_postal_code}, {self.region} - Город {self.city} - {other_street} д. {building}"
            else:
                other_region = random.choice(list(self.REGIONS_CITIES_STREETS.keys()))
                other_city = random.choice(list(self.REGIONS_CITIES_STREETS[other_region].keys()))
                other_street = random.choice(self.REGIONS_CITIES_STREETS[other_region][other_city])
                building = random.randint(1, 300)
                other_postal_code = self.POSTAL_CODES[other_city]
                self._data.actual_address = f"{other_postal_code}, {other_region} - Город {other_city} - {other_street} д. {building}"
        return self._data.actual_address

    @property
    @handle_errors
    def housing_type(self) -> str:
        """
        Суть: Получение типа жилья. Возвращает случайный тип жилья из загруженного
        списка HOUSING_TYPES. При первом обращении выбирает случайное значение.
        Последующие обращения возвращают сохраненное значение из внутреннего хранилища.
        """
        if self._data.housing_type is None:
            self._data.housing_type = random.choice(self.HOUSING_TYPES)
        return self._data.housing_type

    def __str__(self) -> str:
        """
        Суть: Строковое представление всех сгенерированных адресных данных. Формирует
        многострочную строку, содержащую все компоненты адреса: регион, город, улицу,
        адрес регистрации, фактический адрес и тип жилья. Используется для удобного
        вывода всей информации о сгенерированном адресе.
        """
        return (f"Регион: {self.region}\n"
                f"Город: {self.city}\n"
                f"Улица: {self.street}\n"
                f"Адрес регистрации: {self.registration_address}\n"
                f"Фактический адрес: {self.actual_address}\n"
                f"Тип жилья: {self.housing_type}")