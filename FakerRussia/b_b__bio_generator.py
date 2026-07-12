import random
from typing import List
from datetime import datetime
from dataclasses import dataclass
from .b_h__base_generator import BaseGenerator
from FakerRussia.b__additional_algorithms.a_a__handle_errors import handle_errors
from FakerRussia.b__additional_algorithms.a_c__choice_value import choice_value


@dataclass
class _BioData:
    """
    Суть: Внутренний контейнер данных для хранения состояния генератора биографических
    данных. Хранит сгенерированные биографические компоненты (имя, фамилия, отчество,
    имя отца, возраст, дата рождения, пол, рост, национальность, знак зодиака, поколение,
    группа крови, религия, телосложение, цвет глаз, цвет волос, уровень образования,
    размер обуви, вес, индекс массы тела, зрение, слух, группа инвалидности, пульс,
    прививки, военная категория, место учебы, средний балл аттестата) для обеспечения
    согласованности данных при множественных обращениях к свойствам.
    """
    name: str = None
    surname: str = None
    patronymic: str = None
    father_name: str = None
    age: int = None
    year: str = None
    gender: str = None
    height: int = None
    nationality: str = None
    zodiac_sign: str = None
    generation: str = None
    blood_type: str = None
    religion: str = None
    body_type: str = None
    eye_color: str = None
    hair_color: str = None
    education_level: str = None
    shoe_size: str = None
    weight: int = None
    body_mass_index: int | float = None
    vision: str = None
    hearing_status: str = None
    disability_group: str = None
    pulse: int = None
    vaccinations: List[str] | str = None
    military_fitness_category: str = None
    current_place_study: str = None
    average_score_certificate: int | float | str = None


class BioGenerator(BaseGenerator):
    """
    Суть: Генератор биографических данных человека. Предоставляет функциональность
    для генерации различных биографических характеристик: ФИО (имя, фамилия, отчество),
    возраст и дата рождения, пол, физические параметры (рост, вес, размер обуви, индекс
    массы тела), национальность, знак зодиака, поколение, группа крови, религия,
    телосложение, цвет глаз и волос, уровень образования, состояние здоровья (зрение,
    слух, группа инвалидности, пульс, прививки), военная категория годности, место
    учебы, средний балл аттестата. Данные загружаются из JSON-файлов. Поддерживает
    предустановку пола через параметр my_gender и сброс сгенерированных данных.
    """

    def __init__(self, my_gender: str = None):
        """
        Суть: Инициализация генератора биографических данных. Создает экземпляр
        генератора, инициализирует внутреннее хранилище данных _BioData, загружает
        биографические данные из JSON-файлов через метод _load_bio_data. Если
        передан параметр my_gender и он является допустимым значением из списка
        GENDER, устанавливает заданный пол, иначе пол будет выбран случайно при
        первом обращении к свойству gender.
        """
        super().__init__()
        self._data = _BioData()
        self._load_bio_data()
        if isinstance(my_gender, str) and len(my_gender) > 0 and my_gender in self.GENDER:
            self._data.gender = my_gender

    def _load_bio_data(self):
        """
        Суть: Загрузка биографических данных из JSON-файлов. Загружает данные о
        женских именах, фамилиях, отчествах из файлов female_name.json, female_surname.json,
        female_patronymic.json. Загружает данные о мужских именах, фамилиях, отчествах
        из файлов male_name.json, male_surname.json, male_patronymic.json. Загружает
        списки национальностей, поколений, групп крови, религий, типов телосложения,
        цветов глаз, цветов волос, уровней образования, весовых нормативов, прививок,
        школ, колледжей, университетов из соответствующих JSON-файлов. Сохраняет
        загруженные данные в атрибуты класса для дальнейшего использования.
        """
        female_names = self._load_json('a__data/female/female_name.json')
        self.FEMALE_NAMES = female_names.get("FEMALE_NAMES", [])
        female_surnames = self._load_json('a__data/female/female_surname.json')
        self.FEMALE_SURNAMES = female_surnames.get("FEMALE_SURNAMES", [])
        female_patronymics = self._load_json('a__data/female/female_patronymic.json')
        self.FEMALE_PATRONYMICS = female_patronymics.get("FEMALE_PATRONYMICS", {})
        male_names = self._load_json('a__data/male/male_name.json')
        self.MALE_NAMES = male_names.get("MALE_NAMES", [])
        male_surnames = self._load_json('a__data/male/male_surname.json')
        self.MALE_SURNAMES = male_surnames.get("MALE_SURNAMES", [])
        male_patronymics = self._load_json('a__data/male/male_patronymic.json')
        self.MALE_PATRONYMICS = male_patronymics.get("MALE_PATRONYMICS", {})
        nationality_data = self._load_json('a__data/nationality/nationality.json')
        self.NATIONALITIES = nationality_data.get("NATIONALITIES", [])
        generations_data = self._load_json('a__data/generation/generations.json')
        self.GENERATIONS = generations_data.get("GENERATIONS", {})
        blood_types_data = self._load_json('a__data/blood_type/blood_types.json')
        self.BLOOD_TYPES = blood_types_data.get("BLOOD_TYPES", [])
        religions_data = self._load_json('a__data/religion/religions.json')
        self.RELIGIONS = religions_data.get("RELIGIONS", [])
        body_types_data = self._load_json('a__data/body_type/body_types.json')
        self.BODY_TYPES = body_types_data.get("BODY_TYPES", [])
        eye_colors_data = self._load_json('a__data/eye_color/eye_colors.json')
        self.EYE_COLORS = eye_colors_data.get("EYE_COLORS", [])
        hair_colors_data = self._load_json('a__data/hair_color/hair_colors.json')
        self.HAIR_COLORS = hair_colors_data.get("HAIR_COLORS", [])
        education_levels_data = self._load_json('a__data/education_level/education_levels.json')
        self.EDUCATION_LEVELS = education_levels_data.get("EDUCATION_LEVELS", [])
        weights_data = self._load_json('a__data/weight/weights.json')
        self.WEIGHTS = weights_data.get("WEIGHTS", [])
        vaccinations_data = self._load_json('a__data/vaccinations/vaccinations.json')
        self.VACCINATIONS = vaccinations_data.get("VACCINATIONS", [])
        schools_data = self._load_json('a__data/educational_institution/schools.json')
        self.SCHOOLS = schools_data.get("SCHOOLS", [])
        colleges_data = self._load_json('a__data/educational_institution/colleges.json')
        self.COLLEGES = colleges_data.get("COLLEGES", [])
        universities_data = self._load_json('a__data/educational_institution/universities.json')
        self.UNIVERSITIES = universities_data.get("UNIVERSITIES", [])

    def reset(self):
        """
        Суть: Сброс сгенерированных биографических данных. Очищает внутреннее
        хранилище данных, создавая новый экземпляр _BioData, что позволяет
        сгенерировать новый набор биографических компонентов при последующих
        обращениях к свойствам.
        """
        self._data = _BioData()
        return "Биографические данные сброшены"

    @property
    @handle_errors
    def gender(self) -> str:
        """
        Суть: Получение пола человека. Возвращает сгенерированный пол. При первом
        обращении случайным образом выбирает пол из списка GENDER. Последующие
        обращения возвращают сохраненное значение из внутреннего хранилища.
        """
        if self._data.gender is None:
            self._data.gender = random.choice(self.GENDER)
        return self._data.gender

    @property
    @handle_errors
    def age(self) -> int:
        """
        Суть: Получение возраста человека. Возвращает сгенерированный возраст.
        При первом обращении случайным образом выбирает возраст от 1 до 110 лет.
        Последующие обращения возвращают сохраненное значение из внутреннего хранилища.
        """
        if self._data.age is None:
            self._data.age = random.randint(1, 110)
        return self._data.age

    @property
    @handle_errors
    def year(self) -> str:
        """
        Суть: Получение даты рождения. Формирует дату рождения на основе возраста.
        С вероятностью 1/3 использует текущую дату (день и месяц текущего дня),
        иначе генерирует случайную дату (месяц от 1 до 12, день от 1 до 28).
        Год рассчитывается как текущий год минус возраст, с корректировкой если
        случайный месяц больше текущего. Формат: "ДД.ММ.ГГГГ".
        """
        if self._data.year is None:
            now = datetime.now()
            year_answer = now.year - self.age
            if random.choice([True, False, False]):
                self._data.year = f"{now.day:02d}.{now.month:02d}.{year_answer}"
            else:
                month = random.randint(1, 12)
                day = random.randint(1, 28)
                if month > now.month:
                    year_answer -= 1
                self._data.year = f"{day:02d}.{month:02d}.{year_answer}"
        return self._data.year

    @property
    @handle_errors
    def name(self) -> str:
        """
        Суть: Получение имени человека. Возвращает сгенерированное имя.
        При первом обращении в зависимости от пола выбирает имя из списка
        MALE_NAMES (для мужчин) или FEMALE_NAMES (для женщин). Последующие
        обращения возвращают сохраненное значение из внутреннего хранилища.
        """
        if self._data.name is None:
            if self.gender == self.GENDER[0]:
                self._data.name = random.choice(self.MALE_NAMES)
            else:
                self._data.name = random.choice(self.FEMALE_NAMES)
        return self._data.name

    @property
    @handle_errors
    def surname(self) -> str:
        """
        Суть: Получение фамилии человека. Возвращает сгенерированную фамилию.
        При первом обращении в зависимости от пола выбирает фамилию из списка
        MALE_SURNAMES (для мужчин) или FEMALE_SURNAMES (для женщин). Последующие
        обращения возвращают сохраненное значение из внутреннего хранилища.
        """
        if self._data.surname is None:
            if self.gender == self.GENDER[0]:
                self._data.surname = random.choice(self.MALE_SURNAMES)
            else:
                self._data.surname = random.choice(self.FEMALE_SURNAMES)
        return self._data.surname

    @property
    @handle_errors
    def patronymic(self) -> str:
        """
        Суть: Получение отчества человека. Возвращает сгенерированное отчество.
        При первом обращении в зависимости от пола выбирает отчество из ключей
        словаря MALE_PATRONYMICS (для мужчин) или FEMALE_PATRONYMICS (для женщин).
        Последующие обращения возвращают сохраненное значение из внутреннего хранилища.
        """
        if self._data.patronymic is None:
            if self.gender == self.GENDER[0]:
                self._data.patronymic = random.choice(list(self.MALE_PATRONYMICS.keys()))
            else:
                self._data.patronymic = random.choice(list(self.FEMALE_PATRONYMICS.keys()))
        return self._data.patronymic

    @property
    def full_name(self) -> str:
        """
        Суть: Получение полного ФИО человека. Формирует строку с полным именем
        в формате "Фамилия Имя Отчество" на основе сгенерированных фамилии, имени и отчества.
        """
        return f"{self.surname} {self.name} {self.patronymic}"

    @property
    @handle_errors
    def father_name(self) -> str:
        """
        Суть: Получение имени отца. Возвращает имя отца, полученное из словаря
        отчеств (MALE_PATRONYMICS или FEMALE_PATRONYMICS) по отчеству человека.
        При первом обращении сохраняет значение во внутреннем хранилище.
        """
        if self._data.father_name is None:
            if self.gender == self.GENDER[0]:
                self._data.father_name = self.MALE_PATRONYMICS[self.patronymic]
            else:
                self._data.father_name = self.FEMALE_PATRONYMICS[self.patronymic]
        return self._data.father_name

    @property
    @handle_errors
    def full_name_father(self) -> str:
        """
        Суть: Получение полного ФИО отца. Формирует ФИО отца на основе фамилии
        человека (с преобразованием в мужскую форму при необходимости) и имени
        отца. Отчество отца выбирается случайно из мужских отчеств. С вероятностью
        30% добавляет пометку " (ушёл из семьи)".
        """
        name = self.father_name
        patronymic = random.choice(list(self.MALE_PATRONYMICS.keys()))
        if self.gender == self.GENDER[0]:
            surname = self._data.surname
        else:
            if self._data.surname.endswith('а'):
                surname = self._data.surname[:-1]
            else:
                try:
                    idx = self.FEMALE_SURNAMES.index(self._data.surname)
                    surname = self.MALE_SURNAMES[idx]
                except ValueError:
                    surname = self._data.surname
        text = f"{surname} {name} {patronymic}"
        if random.random() < 0.3:
            text += " (ушёл из семьи)"
        return text

    @property
    @handle_errors
    def full_name_mother(self) -> str:
        """
        Суть: Получение полного ФИО матери. Формирует ФИО матери с девичьей фамилией.
        Имя и отчество матери выбираются случайно из женских имен и отчеств. Фамилия
        формируется на основе фамилии человека (с преобразованием в женскую форму
        при необходимости). Девичья фамилия выбирается случайно из женских фамилий.
        С вероятностью 30% добавляет пометку " (ушла из семьи)".
        """
        name = random.choice(self.FEMALE_NAMES)
        patronymic = random.choice(list(self.FEMALE_PATRONYMICS.keys()))
        if self.gender == self.GENDER[0]:
            try:
                idx = self.MALE_SURNAMES.index(self._data.surname)
                surname = self.FEMALE_SURNAMES[idx]
            except ValueError:
                surname = self._data.surname + 'а'
        else:
            surname = self._data.surname
        maiden_name = random.choice(self.FEMALE_SURNAMES)
        text = f"{surname} (девичья фамилия - {maiden_name}) {name} {patronymic}"
        if random.random() < 0.3:
            text += " (ушла из семьи)"
        return text

    @property
    @handle_errors
    def nationality(self) -> str:
        """
        Суть: Получение национальности. Возвращает случайную национальность из
        загруженного списка NATIONALITIES. Использует вспомогательную функцию
        choice_value для обеспечения согласованности данных.
        """
        return choice_value(
            value=self._data.nationality,
            variants=self.NATIONALITIES
        )

    @property
    @handle_errors
    def zodiac_sign(self) -> str:
        """
        Суть: Получение знака зодиака. Вычисляет знак зодиака на основе
        даты рождения (месяца и дня) из свойства year. Определяет знак по
        стандартным астрологическим диапазонам. Результат сохраняется во
        внутреннем хранилище.
        """
        if self._data.zodiac_sign is None:
            date = self.year.split(".")
            month = int(date[1])
            day = int(date[0])
            if (month == 3 and day >= 21) or (month == 4 and day <= 19):
                self._data.zodiac_sign = self.ZODIAC_SIGNS[0]
            elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
                self._data.zodiac_sign = self.ZODIAC_SIGNS[1]
            elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
                self._data.zodiac_sign = self.ZODIAC_SIGNS[2]
            elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
                self._data.zodiac_sign = self.ZODIAC_SIGNS[3]
            elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
                self._data.zodiac_sign = self.ZODIAC_SIGNS[4]
            elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
                self._data.zodiac_sign = self.ZODIAC_SIGNS[5]
            elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
                self._data.zodiac_sign = self.ZODIAC_SIGNS[6]
            elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
                self._data.zodiac_sign = self.ZODIAC_SIGNS[7]
            elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
                self._data.zodiac_sign = self.ZODIAC_SIGNS[8]
            elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
                self._data.zodiac_sign = self.ZODIAC_SIGNS[9]
            elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
                self._data.zodiac_sign = self.ZODIAC_SIGNS[10]
            else:
                self._data.zodiac_sign = self.ZODIAC_SIGNS[11]
        return self._data.zodiac_sign

    @property
    @handle_errors
    def generation(self) -> str:
        """
        Суть: Получение названия поколения. Определяет поколение человека
        на основе года рождения по классификации поколений из словаря
        GENERATIONS. Год рождения извлекается из свойства year. Если год
        не попадает ни в один диапазон, возвращает "Данного поколения не найдено".
        """
        if self._data.generation is None:
            year = int(self.year.split(".")[2])
            for key, value in self.GENERATIONS.items():
                range_years = key.split("-")
                if int(range_years[0]) <= year <= int(range_years[1]):
                    self._data.generation = value
                    break
            if self._data.generation is None:
                self._data.generation = "Данного поколения не найдено"
        return self._data.generation

    @property
    @handle_errors
    def blood_type(self) -> str:
        """
        Суть: Получение группы крови. Возвращает случайную группу крови
        из загруженного списка BLOOD_TYPES. Использует вспомогательную
        функцию choice_value для обеспечения согласованности данных.
        """
        return choice_value(
            value=self._data.blood_type,
            variants=self.BLOOD_TYPES
        )

    @property
    @handle_errors
    def religion(self) -> str:
        """
        Суть: Получение вероисповедания. Возвращает случайную религию из
        загруженного списка RELIGIONS. Использует вспомогательную функцию
        choice_value для обеспечения согласованности данных.
        """
        return choice_value(
            value=self._data.religion,
            variants=self.RELIGIONS
        )

    @property
    @handle_errors
    def body_type(self) -> str:
        """
        Суть: Получение типа телосложения. Возвращает случайный тип
        телосложения из загруженного списка BODY_TYPES. Использует
        вспомогательную функцию choice_value для обеспечения
        согласованности данных.
        """
        return choice_value(
            value=self._data.body_type,
            variants=self.BODY_TYPES
        )

    @property
    @handle_errors
    def eye_color(self) -> str:
        """
        Суть: Получение цвета глаз. Возвращает случайный цвет глаз из
        загруженного списка EYE_COLORS. Использует вспомогательную функцию
        choice_value для обеспечения согласованности данных.
        """
        return choice_value(
            value=self._data.eye_color,
            variants=self.EYE_COLORS
        )

    @property
    @handle_errors
    def hair_color(self) -> str:
        """
        Суть: Получение цвета волос. С вероятностью 10% возвращает
        "Данный человек лысый". В остальных случаях возвращает случайный
        цвет волос из загруженного списка HAIR_COLORS. Результат сохраняется
        во внутреннем хранилище.
        """
        if self._data.hair_color is None:
            if random.random() < 0.1:
                self._data.hair_color = "Данный человек лысый"
            else:
                self._data.hair_color = random.choice(self.HAIR_COLORS)
        return self._data.hair_color

    @property
    @handle_errors
    def education_level(self) -> str:
        """
        Суть: Получение уровня образования. Определяет уровень образования
        в зависимости от возраста. Для детей до 5 лет возвращает
        соответствующий ответ из SMALL_AGE_ANSWERS. Для школьного возраста
        (7-16 лет) возвращает начальное или основное общее образование.
        Для старшего школьного возраста и студентов (16-22 года) возвращает
        среднее общее, начальное профессиональное или среднее профессиональное
        образование. Для взрослых (23-70 лет) возвращает случайный уровень из
        списка EDUCATION_LEVELS[11:]. Для пенсионеров (старше 70 лет) с
        вероятностью 20% возвращает случайный уровень образования, иначе
        возвращает значение PENSION.
        """
        if self._data.education_level is None:
            few_vars = random.choice(self.EDUCATION_LEVELS[11:])
            if self.age < 5:
                self._data.education_level = self.SMALL_AGE_ANSWERS[4]
            elif 7 <= self.age < 11:
                self._data.education_level = self.EDUCATION_LEVELS[0]
            elif 11 <= self.age < 16:
                self._data.education_level = self.EDUCATION_LEVELS[1]
            elif 16 <= self.age < 20:
                self._data.education_level = random.choice(self.EDUCATION_LEVELS[2:5])
            elif 20 <= self.age < 22:
                self._data.education_level = random.choice(self.EDUCATION_LEVELS[5:11])
            elif 23 <= self.age <= 70:
                self._data.education_level = few_vars
            elif self.age > 70:
                if random.random() < 0.2:
                    self._data.education_level = few_vars
                else:
                    self._data.education_level = self.PENSION
        return self._data.education_level


    @property
    @handle_errors
    def height(self) -> int:
        """
        Суть: Получение роста человека. Генерирует рост в зависимости от
        возраста и пола, используя возрастные нормативы. Для детей до
        14 лет используются стандартные диапазоны роста по возрастам.
        Для подростков (14-17 лет) используются диапазоны в зависимости
        от пола. Для взрослых (18 лет и старше) используются расширенные
        диапазоны: для мужчин от 152 до 210 см, для женщин от 145 до 195 см.
        """
        if self._data.height is None:
            if self.age == 1:
                self._data.height = random.randint(50, 76)
            elif self.age == 2:
                self._data.height = random.randint(76, 96)
            elif 3 <= self.age < 7:
                self._data.height = random.randint(96, 122)
            elif 7 <= self.age < 11:
                self._data.height = random.randint(122, 143)
            elif 11 <= self.age < 14:
                self._data.height = random.randint(143, 162)
            elif 14 <= self.age < self.AGE_MAJORITY and self.gender == self.GENDER[0]:
                self._data.height = random.randint(162, 177)
            elif 14 <= self.age < self.AGE_MAJORITY and self.gender == self.GENDER[1]:
                self._data.height = random.randint(159, 166)
            elif self.age >= self.AGE_MAJORITY and self.gender == self.GENDER[0]:
                self._data.height = random.randint(152, 210)
            elif self.age >= self.AGE_MAJORITY and self.gender == self.GENDER[1]:
                self._data.height = random.randint(145, 195)
        return self._data.height

    @property
    @handle_errors
    def shoe_size(self) -> str:
        """
        Суть: Получение размера обуви. Генерирует размер обуви в зависимости
        от возраста и пола. Для взрослых (18 лет и старше): мужчины - от 38
        до 50, женщины - от 33 до 42. Для детей и подростков - от 20 до 37.
        """
        if self._data.shoe_size is None:
            if self.age >= self.AGE_MAJORITY:
                if self.gender == self.GENDER[0]:
                    self._data.shoe_size = str(random.randint(38, 50))
                else:
                    self._data.shoe_size = str(random.randint(33, 42))
            else:
                self._data.shoe_size = str(random.randint(20, 37))
        return self._data.shoe_size

    @property
    @handle_errors
    def weight(self) -> int:
        """
        Суть: Получение веса человека. Генерирует вес на основе возрастных
        нормативов из загруженного списка WEIGHTS. Для возрастов до 18 лет
        использует нормативные диапазоны из WEIGHTS. Для взрослых (старше 18 лет)
        генерирует вес в зависимости от пола: мужчины - от 55 до 100 кг,
        женщины - от 48 до 86 кг.
        """
        if self._data.weight is None:
            for weight in range(len(self.WEIGHTS)):
                age = self.age - 1
                if self.age <= len(self.WEIGHTS):
                    answer = self.WEIGHTS[age]
                    self._data.weight = random.randint(answer[0], answer[1])
                    return self._data.weight
                else:
                    if self.gender == self.GENDER[0]:
                        self._data.weight = random.randint(55, 100)
                    elif self.gender == self.GENDER[1]:
                        self._data.weight = random.randint(48, 86)
                    return self._data.weight
        return self._data.weight

    @property
    @handle_errors
    def body_mass_index(self) -> str:
        """
        Суть: Получение индекса массы тела (ИМТ). Вычисляет ИМТ на основе
        веса и роста по формуле: вес / (рост/100)². Результат возвращается
        в виде строки с двумя знаками после запятой.
        """
        if self._data.body_mass_index is None:
            decision = self.weight / (self.height / 100) ** 2
            self._data.body_mass_index = f"{decision:.2f}"
        return self._data.body_mass_index

    @property
    @handle_errors
    def vision(self) -> str:
        """
        Суть: Получение показателя зрения. С вероятностью 30% возвращает
        "Отличное зрение". В остальных случаях генерирует случайное значение
        от 0.0 до 6.0 с одним знаком после запятой и случайным знаком плюс
        или минус. Формат: "+X.X" или "-X.X".
        """
        if self._data.vision is None:
            if random.random() < 0.3:
                self._data.vision = "Отличное зрение"
                return self._data.vision

            answer = f"{random.uniform(0.0, 6.0):.1f}"
            self._data.vision = f"{random.choice(['+', '-'])}{answer}"
        return self._data.vision

    @property
    @handle_errors
    def hearing_status(self) -> str:
        """
        Суть: Получение состояния слуха. Возвращает случайный статус слуха
        из загруженного списка HEARING_STATUS. Использует вспомогательную
        функцию choice_value для обеспечения согласованности данных.
        """
        return choice_value(
            value=self._data.hearing_status,
            variants=self.HEARING_STATUS
        )

    @property
    @handle_errors
    def disability_group(self) -> str:
        """
        Суть: Получение группы инвалидности. С вероятностью 30% присваивает
        группу инвалидности. Для несовершеннолетних возвращает "Категория 'ребёнок-инвалид'".
        Для взрослых возвращает случайную группу из списка DISABILITY_DEGREES. С вероятностью
        70% возвращает "Отсутствует".
        """
        if self._data.disability_group is None:
            if random.random() < 0.3:
                if self._data.age < self.AGE_MAJORITY:
                    self._data.disability_group = "Категория 'ребёнок-инвалид'"
                    return self._data.disability_group
                self._data.disability_group = random.choice(self.DISABILITY_DEGREES)
                return self._data.disability_group
            self._data.disability_group = "Отсутствует"
        return self._data.disability_group

    @property
    @handle_errors
    def pulse(self) -> int:
        """
        Суть: Получение пульса в состоянии покоя. Генерирует пульс в зависимости от
        возраста по возрастным нормативам: для детей 1-6 лет - 95-120 уд/мин, 7-11 лет
        - 80-95 уд/мин, 12-17 лет - 65-85 уд/мин, взрослые 18-49 лет - 60-80 уд/мин,
        50-69 лет - 65-85 уд/мин, старше 70 лет - 70-90 уд/мин.
        """
        if self._data.pulse is None:
            if 1 <= self._data.age < 7:
                self._data.pulse = random.randint(95, 120)
            elif 7 <= self._data.age < 12:
                self._data.pulse = random.randint(80, 95)
            elif 12 <= self._data.age < self.AGE_MAJORITY:
                self._data.pulse = random.randint(65, 85)
            elif self.AGE_MAJORITY <= self._data.age < 50:
                self._data.pulse = random.randint(60, 80)
            elif 50 <= self._data.age < 70:
                self._data.pulse = random.randint(65, 85)
            else:
                self._data.pulse = random.randint(70, 90)
        return self._data.pulse

    @handle_errors
    def vaccinations(self, visualization: bool = False) -> List[str] | str:
        """
        Суть: Получение списка прививок. С вероятностью 30% возвращает "Нет ни одной".
        В остальных случаях генерирует список из 1-5 случайных прививок из загруженного
        списка VACCINATIONS. Если параметр visualization=True, возвращает строку с
        прививками через запятую, иначе возвращает список.
        """
        if self._data.vaccinations is None:
            if random.random() < 0.3:
                self._data.vaccinations = "Нет ни одной"
                return self._data.vaccinations
            vac_lst = [random.choice(self.VACCINATIONS) for _ in range(random.randint(1, 5))]
            self._data.vaccinations = vac_lst
        if visualization:
            return ", ".join(self._data.vaccinations)
        return self._data.vaccinations

    @property
    @handle_errors
    def military_fitness_category(self) -> str:
        """
        Суть: Получение военной категории годности. Для женщин возвращает
        "Данный человек не подходит по полу". Для мужчин младше 17 лет
        возвращает соответствующий ответ из SMALL_AGE_ANSWERS[12]. Для мужчин
        призывного возраста возвращает случайную категорию из ключей словаря DISEASES.
        """
        if self._data.military_fitness_category is None:
            if self.gender == self.GENDER[1]:
                self._data.military_fitness_category = "Данный человек не подходит по полу"
            elif self.gender == self.GENDER[0] and self.age < 17:
                self._data.military_fitness_category = self.SMALL_AGE_ANSWERS[12]
            self._data.military_fitness_category = random.choice(list(self.DISEASES.keys()))
        return self._data.military_fitness_category

    @property
    @handle_errors
    def current_place_study(self) -> str:
        """
        Суть: Получение текущего места учебы. Определяет место учебы в зависимост
        от уровня образования. Для детей до 5 лет возвращает ответ из SMALL_AGE_ANSWERS[4].
        Для школьников (начальное, основное, среднее общее образование) возвращает
        случайную школу с номером. Для студентов колледжа возвращает случайный колледж.
        Для лиц с высшим образованием возвращает случайный университет. Для пенсионеров
        возвращает значение PENSION. Для некоторых уровней образования возвращает
        значение N_A_STUDY_PLACE.
        """
        if self._data.current_place_study is None:
            if self.age < 5:
                self._data.current_place_study = self.SMALL_AGE_ANSWERS[4]
            elif self.education_level in self.EDUCATION_LEVELS[:3]:
                self._data.current_place_study = f"{random.choice(self.SCHOOLS)} №{random.randint(1, 200)}"
            elif self.education_level == self.EDUCATION_LEVELS[3]:
                self._data.current_place_study = random.choice(self.COLLEGES)
            elif self.education_level == self.EDUCATION_LEVELS[4] or \
                    self.education_level == self.EDUCATION_LEVELS[15]:
                self._data.current_place_study = self.N_A_STUDY_PLACE
            elif self.education_level in self.EDUCATION_LEVELS[5:15]:
                self._data.current_place_study = random.choice(self.UNIVERSITIES)
            elif self.education_level == self.PENSION:
                self._data.current_place_study = self.PENSION
        return self._data.current_place_study

    @property
    @handle_errors
    def average_score_certificate(self) -> int | float | str:
        """
        Суть: Получение среднего балла аттестата. Если человек еще учится в
        школе (уровень образования в EDUCATION_LEVELS[:3]), возвращает
        сообщение "Данный человек ещё пока учится и не имеет средний балл
        аттестата". В остальных случаях генерирует случайный балл от 2.50
        до 5.00 с двумя знаками после запятой.
        """
        if self._data.average_score_certificate is None:
            if self.education_level in self.EDUCATION_LEVELS[:3]:
                self._data.average_score_certificate = "Данный человек ещё пока учится и не имеет средний балл аттестата"
            else:
                self._data.average_score_certificate = f"{random.randint(250, 500) / 100:.2f}"
        return self._data.average_score_certificate

    def __str__(self) -> str:
        """
        Суть: Строковое представление всех сгенерированных биографических данных.
        Формирует многострочную строку, содержащую все биографические компоненты:
        ФИО, дата рождения, возраст, пол, ФИО отца, ФИО матери, национальность,
        рост, вес, индекс массы тела, знак зодиака, поколение, группа крови, религия,
        телосложение, цвет глаз, цвет волос, образование, средний балл аттестата,
        место учебы, размер обуви, зрение, слух, инвалидность, пульс, прививки,
        военная категория годности.
        """
        return (f"ФИО: {self.full_name}\n"
                f"Год рождения: {self.year}\n"
                f"Возраст: {self.age}\n"
                f"Пол: {self.gender}\n"
                f"ФИО отца: {self.full_name_father}\n"
                f"ФИО матери: {self.full_name_mother}\n"
                f"Национальность: {self.nationality}\n"
                f"Рост: {self.height}\n"
                f"Вес: {self.weight}\n"
                f"Индекс массы тела: {self.body_mass_index}\n"
                f"Знак зодиака: {self.zodiac_sign}\n"
                f"Поколение: {self.generation}\n"
                f"Группа крови: {self.blood_type}\n"
                f"Религия: {self.religion}\n"
                f"Телосложение: {self.body_type}\n"
                f"Цвет глаз: {self.eye_color}\n"
                f"Цвет волос: {self.hair_color}\n"
                f"Образование: {self.education_level}\n"
                f"Средний балл школьного аттестата: {self.average_score_certificate}\n"
                f"Текущее место обучения: {self.current_place_study}\n"
                f"Размер обуви: {self.shoe_size}\n"
                f"Зрение: {self.vision}\n"
                f"Уровень слуха: {self.hearing_status}\n"
                f"Инвалидность: {self.disability_group}\n"
                f"Пульс в покое: {self.pulse}\n"
                f"Прививки (вакцинации): {self.vaccinations()}\n"
                f"Военная категория годности: {self.military_fitness_category}")