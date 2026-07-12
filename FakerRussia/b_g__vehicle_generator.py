import random
from typing import List
from datetime import datetime
from dataclasses import dataclass
from .b_h__base_generator import BaseGenerator
from FakerRussia.b__additional_algorithms.a_a__handle_errors import handle_errors
from FakerRussia.b__additional_algorithms.a_f__characteristics_car import characteristics_car


@dataclass
class _VehicleData:
    """
    Суть: Внутренний контейнер данных для хранения состояния генератора транспортных
    данных. Хранит сгенерированные транспортные компоненты (марка и модель автомобиля,
    государственный регистрационный номер, наличие автомобиля, состояние автомобиля,
    цвет автомобиля, год выпуска, тип кузова, тип двигателя, объем двигателя, тип
    трансмиссии, тип привода, мощность двигателя) для обеспечения согласованности
    данных при множественных обращениях к свойствам.
    """
    car: str = None
    car_registration_number: str = None
    has_car: bool = None
    car_condition_type: List[str] | str = None
    car_color: str = None
    car_year: int = None
    car_body_type: str = None
    machine_engine_type: str = None
    engine_capacity: float | int = None
    transmission_type: str = None
    machine_drive: str = None
    engine_power: int = None


class VehicleGenerator(BaseGenerator):
    """
    Суть: Генератор транспортных данных человека. Предоставляет функциональность для генерации
    различных характеристик автомобиля: марка и модель, наличие автомобиля, государственный
    регистрационный номер (с кодом региона), состояние автомобиля (повреждения, дефекты), цвет,
    год выпуска, технические характеристики (тип кузова, тип двигателя, объем двигателя, тип
    трансмиссии, тип привода, мощность двигателя). Данные загружаются из JSON-файлов. Для генерации
    использует информацию из переданных генераторов биографии и адреса.
    """

    def __init__(self, bio, address):
        """
        Суть: Инициализация генератора транспортных данных. Создает экземпляр генератора,
        сохраняет ссылки на генераторы биографии (bio) и адреса (address) для использования
        их данных. Инициализирует внутреннее хранилище данных _VehicleData и загружает транспортные
        данные из JSON-файлов через метод _load_vehicle_data.
        """
        super().__init__()
        self._bio = bio
        self._address = address
        self._data = _VehicleData()
        self._load_vehicle_data()

    def _load_vehicle_data(self):
        """
        Суть: Загрузка транспортных данных из JSON-файлов. Загружает список марок и моделей
        автомобилей с их характеристиками из файла 'a__data/car/cars.json', коды регионов для
        госномеров из файла 'a__data/car/regions_gos_codes.json', типы состояния автомобиля
        (повреждения, дефекты) из файла 'a__data/car/car_condition_types.json', цвета автомобилей
        из файла 'a__data/car/car_colors.json'. Сохраняет загруженные данные в атрибуты класса
        для дальнейшего использования.
        """
        cars_data = self._load_json('a__data/car/cars.json')
        self.CARS = cars_data.get("CARS", {})
        regions_gos_codes_data = self._load_json('a__data/car/regions_gos_codes.json')
        self.REGIONS_GOS_CODES = regions_gos_codes_data.get("REGIONS_GOS_CODES", {})
        car_condition_types_data = self._load_json('a__data/car/car_condition_types.json')
        self.CAR_CONDITION_TYPES = car_condition_types_data.get("CAR_CONDITION_TYPES", [])
        car_colors_data = self._load_json('a__data/car/car_colors.json')
        self.CAR_COLORS = car_colors_data.get("CAR_COLORS", [])

    def reset(self):
        """
        Суть: Сброс сгенерированных транспортных данных. Очищает внутреннее хранилище данных,
        создавая новый экземпляр _VehicleData, что позволяет сгенерировать новый набор
        транспортных компонентов при последующих обращениях к свойствам.
        """
        self._data = _VehicleData()
        return "Транспортные данные сброшены"

    @property
    def has_car(self) -> bool:
        """
        Суть: Получение статуса наличия автомобиля. Возвращает значение из внутреннего хранилища,
        если оно установлено, иначе возвращает False. Статус устанавливается в свойстве car при
        генерации марки автомобиля.
        """
        return self._data.has_car if self._data.has_car is not None else False

    @property
    @handle_errors
    def car(self) -> str:
        """
        Суть: Получение марки и модели автомобиля. Для лиц младше 16 лет устанавливает has_car = False
        и возвращает соответствующий ответ из SMALL_AGE_ANSWERS[3]. Для остальных с вероятностью 50%
        выбирает случайную марку и модель из списка CARS, устанавливает has_car = True, иначе
        устанавливает has_car = False и возвращает значение N_A_CAR. Результат сохраняется во
        внутреннем хранилище.
        """
        if self._data.car is None:
            if self._bio.age < 16:
                self._data.has_car = False
                self._data.car = self.SMALL_AGE_ANSWERS[3]
            elif random.choice([True, False]):
                model = random.choice(list(self.CARS.keys()))
                self._data.has_car = True
                self._data.car = model
            else:
                self._data.has_car = False
                self._data.car = self.N_A_CAR
        return self._data.car

    @property
    @handle_errors
    def car_body_type(self) -> str:
        """
        Суть: Получение типа кузова автомобиля. Использует вспомогательную функцию characteristics_car
        с параметром number_attr=0. Если автомобиль отсутствует, возвращает N_A_CAR. Если автомобиль
        есть, возвращает тип кузова из характеристик выбранной модели в словаре CARS.
        """
        return characteristics_car(
            value=self._data.car_body_type,
            has_car=self._data.has_car,
            car_model=self.car,
            lst_cars=self.CARS,
            n_a_car=self.N_A_CAR,
            number_attr=0
        )

    @property
    @handle_errors
    def machine_engine_type(self) -> str:
        """
        Суть: Получение типа двигателя автомобиля. Использует вспомогательную функцию characteristics_car
        с параметром number_attr=1. Если автомобиль отсутствует, возвращает N_A_CAR. Если автомобиль есть,
        возвращает тип двигателя из характеристик выбранной модели в словаре CARS (бензиновый, дизельный,
        электрический, гибридный и т.д.).
        """
        return characteristics_car(
            value=self._data.machine_engine_type,
            has_car=self._data.has_car,
            car_model=self.car,
            lst_cars=self.CARS,
            n_a_car=self.N_A_CAR,
            number_attr=1
        )

    @property
    @handle_errors
    def engine_capacity(self) -> float | int:
        """
        Суть: Получение объема двигателя автомобиля (в литрах). Использует вспомогательную функцию
        characteristics_car с параметром number_attr=2. Если автомобиль отсутствует, возвращает N_A_CAR.
        Если автомобиль есть, возвращает объем двигателя из характеристик выбранной модели в словаре CARS.
        """
        return characteristics_car(
            value=self._data.engine_capacity,
            has_car=self._data.has_car,
            car_model=self.car,
            lst_cars=self.CARS,
            n_a_car=self.N_A_CAR,
            number_attr=2
        )

    @property
    @handle_errors
    def transmission_type(self) -> str:
        """
        Суть: Получение типа трансмиссии автомобиля. Использует вспомогательную функцию characteristics_car
        с параметром number_attr=3. Если автомобиль отсутствует, возвращает N_A_CAR. Если автомобиль есть,
        возвращает тип трансмиссии из характеристик выбранной модели в словаре CARS (механическая,
        автоматическая, роботизированная, вариатор).
        """
        return characteristics_car(
            value=self._data.transmission_type,
            has_car=self._data.has_car,
            car_model=self.car,
            lst_cars=self.CARS,
            n_a_car=self.N_A_CAR,
            number_attr=3
        )

    @property
    @handle_errors
    def machine_drive(self) -> str:
        """
        Суть: Получение типа привода автомобиля. Использует вспомогательную функцию characteristics_car
        с параметром number_attr=4. Если автомобиль отсутствует, возвращает N_A_CAR. Если автомобиль есть,
        возвращает тип привода из характеристик выбранной модели в словаре CARS (передний, задний, полный).
        """
        return characteristics_car(
            value=self._data.machine_drive,
            has_car=self._data.has_car,
            car_model=self.car,
            lst_cars=self.CARS,
            n_a_car=self.N_A_CAR,
            number_attr=4
        )

    @property
    @handle_errors
    def engine_power(self) -> int:
        """
        Суть: Получение мощности двигателя автомобиля (в лошадиных силах). Использует вспомогательную
        функцию characteristics_car с параметром number_attr=5. Если автомобиль отсутствует, возвращает
        N_A_CAR. Если автомобиль есть, возвращает мощность двигателя из характеристик выбранной модели в
        словаре CARS.
        """
        return characteristics_car(
            value=self._data.engine_power,
            has_car=self._data.has_car,
            car_model=self.car,
            lst_cars=self.CARS,
            n_a_car=self.N_A_CAR,
            number_attr=5
        )

    @property
    @handle_errors
    def car_registration_number(self) -> str:
        """
        Суть: Получение государственного регистрационного номера автомобиля. Если автомобиль
        отсутствует, возвращает N_A_CAR. Если автомобиль есть, формирует номер в формате "Б000ББ 00".
        Буквы (3 штуки) выбираются случайным образом из списка LETTERS_NUMBER_CAR (разрешенные буквы
        для госномеров). Цифры (3 штуки) - случайное число от 1 до 999 с ведущими нулями. Код региона
        выбирается случайным образом из списка REGIONS_GOS_CODES по названию региона. Результат
        сохраняется во внутреннем хранилище.
        """
        if self._data.car_registration_number is None:
            if self._data.has_car:
                region_code = random.choice(self.REGIONS_GOS_CODES[self._address.region])
                numbers = f"{random.randint(1, 999):03d}"
                letters = [random.choice(self.LETTERS_NUMBER_CAR) for _ in range(3)]
                self._data.car_registration_number = f"{letters[0]}{numbers}{letters[1]}{letters[2]} {region_code}"
            else:
                self._data.car_registration_number = self.N_A_CAR
        return self._data.car_registration_number

    @handle_errors
    def car_condition_type(self, visualization: bool = False) -> List[str] | str:
        """
        Суть: Получение списка повреждений и дефектов автомобиля. Если автомобиль отсутствует,
        возвращает N_A_CAR. Если автомобиль есть, с вероятностью 50% возвращает "В идеальном
        состоянии" (CAR_CONDITION_TYPES[0]), иначе генерирует список из 1-4 случайных повреждений/дефектов
        из списка CAR_CONDITION_TYPES[1:]. Если параметр visualization=True, возвращает строку с
        элементами через запятую, иначе возвращает список. Результат сохраняется во внутреннем хранилище.
        """
        if self._data.car_condition_type is None:
            if self._data.has_car:
                if random.choice([True, False]):
                    answer_lst = []
                    for _ in range(random.randint(1, 4)):
                        answer_lst.append(random.choice(self.CAR_CONDITION_TYPES[1:]))
                    self._data.car_condition_type = answer_lst
                else:
                    self._data.car_condition_type = self.CAR_CONDITION_TYPES[0]
            else:
                self._data.car_condition_type = self.N_A_CAR
        if visualization:
            return ", ".join(self._data.car_condition_type)
        return self._data.car_condition_type

    @property
    @handle_errors
    def car_color(self) -> str:
        """
        Суть: Получение цвета автомобиля. Если автомобиль отсутствует, возвращает N_A_CAR.
        Если автомобиль есть, возвращает случайный цвет из списка CAR_COLORS. Результат
        сохраняется во внутреннем хранилище.
        """
        if self._data.car_color is None:
            if self._data.has_car:
                self._data.car_color = random.choice(self.CAR_COLORS)
                return self._data.car_color
            else:
                self._data.car_color = self.N_A_CAR
        return self._data.car_color

    @property
    @handle_errors
    def car_year(self) -> int:
        """
        Суть: Получение года выпуска автомобиля. Если автомобиль отсутствует, возвращает
        N_A_CAR. Если автомобиль есть, возвращает случайный год выпуска от 1990 до текущего
        года. Результат сохраняется во внутреннем хранилище.
        """
        if self._data.car_year is None:
            if self._data.has_car:
                self._data.car_year = random.randint(1990, datetime.now().year)
                return self._data.car_year
            else:
                self._data.car_year = self.N_A_CAR
        return self._data.car_year

    def __str__(self) -> str:
        """
        Суть: Строковое представление всех сгенерированных транспортных данных. Формирует
        многострочную строку, содержащую все транспортные компоненты: марка и модель
        автомобиля, тип кузова, тип двигателя, объем двигателя, тип трансмиссии, тип привода,
        мощность двигателя, государственный регистрационный номер, повреждения и дефекты, цвет,
        год выпуска. Используется для удобного вывода всей информации о сгенерированных транспортных данных.
        """
        return (f"Машина: {self.car}\n"
                f"Тип кузова: {self.car_body_type}\n"
                f"Тип двигателя: {self.machine_engine_type}\n"
                f"Объем двигателя: {self.engine_capacity}\n"
                f"Тип трансмиссии: {self.transmission_type}\n"
                f"Привод: {self.machine_drive}\n"
                f"Мощность двигателя: {self.engine_power}\n"
                f"Номер машины: {self.car_registration_number}\n"
                f"Повреждение: {self.car_condition_type()}\n"
                f"Цвет: {self.car_color}\n"
                f"Год выпуска: {self.car_year}")