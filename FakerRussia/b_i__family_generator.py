import random
from datetime import datetime
from typing import List
from dataclasses import dataclass
from .b_h__base_generator import BaseGenerator
from FakerRussia.b__additional_algorithms.a_a__handle_errors import handle_errors
from FakerRussia.b__additional_algorithms.a_b__choice_machine_family import choice_machine_family
from FakerRussia.b__additional_algorithms.a_e__check_spouse import check_spouse


@dataclass
class _FamilyData:
    """
    Суть: Внутренний контейнер данных для хранения состояния генератора семейных данных. Хранит
    сгенерированные семейные компоненты (семейный статус, фамилия супруга, имя супруга, отчество
    супруга, возраст супруга, дата бракосочетания, количество лет в браке, количество детей,
    имена детей, проживание с родителями, количество членов семьи, сообщение об отсутствии супруга,
    флаг о предыдущем браке супруга) для обеспечения согласованности данных при множественных
    обращениях к свойствам.
    """
    marital_status: str = None
    spouse_surname: str = None
    spouse_name: str = None
    spouse_patronymic: str = None
    spouse_age: int | str = None
    marriage_date: str = None
    years_marriage: int | str = None
    children_count: int | str = None
    children_names: List[str] | str = None
    living_with_parents: bool = None
    family_members_count: int | str = None
    no_spouse_message: str = None
    spouse_was_married: bool = False


class FamilyGenerator(BaseGenerator):
    """
    Суть: Генератор семейных данных человека. Предоставляет функциональность для генерации
    различных семейных характеристик: семейный статус, данные о супруге (ФИО, возраст), дата
    бракосочетания, количество лет в браке, количество детей, имена детей, проживание с
    родителями, количество членов семьи. Данные загружаются из JSON-файлов. Для генерации
    использует информацию из переданных генераторов биографии и финансов.
    """

    def __init__(self, bio, finance):
        """
        Суть: Инициализация генератора семейных данных. Создает экземпляр генератора,
        сохраняет ссылки на генераторы биографии (bio) и финансов (finance) для
        использования их данных. Инициализирует внутреннее хранилище данных _FamilyData,
        загружает семейные данные из JSON-файлов через метод _load_family_data,
        устанавливает начальное значение флага наличия супруга.
        """
        super().__init__()
        self._data = _FamilyData()
        self._bio = bio
        self._finance = finance
        self._load_family_data()
        self._spouse_exists = None

    def _load_family_data(self):
        """
        Суть: Загрузка семейных данных из JSON-файлов. Загружает женские имена, фамилии,
        отчества из файлов female_name.json, female_surname.json, female_patronymic.json.
        Загружает мужские имена, фамилии, отчества из файлов male_name.json, male_surname.json,
        male_patronymic.json. Загружает списки семейных статусов для мужчин и женщин из файла
        'a__data/marital_status/marital_statuses.json'. Сохраняет загруженные данные в атрибуты
        класса для дальнейшего использования.
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
        marital_statuses_data = self._load_json('a__data/marital_status/marital_statuses.json')
        self.MALE_MARITAL_STATUSES = marital_statuses_data.get("MALE_MARITAL_STATUSES", [])
        self.FEMALE_MARITAL_STATUSES = marital_statuses_data.get("FEMALE_MARITAL_STATUSES", [])

    def reset(self):
        """
        Суть: Сброс сгенерированных семейных данных. Очищает внутреннее хранилище данных,
        создавая новый экземпляр _FamilyData, сбрасывает флаг наличия супруга, что
        позволяет сгенерировать новый набор семейных компонентов при последующих обращениях
        к свойствам.
        """
        self._data = _FamilyData()
        self._spouse_exists = None
        return "Семейные данные сброшены"

    def _check_spouse_exists(self):
        """
        Суть: Проверка наличия супруга. Для несовершеннолетних возвращает False и
        устанавливает сообщение об отсутствии супруга. Для совершеннолетних проверяет
        семейный статус: если статус соответствует "Никогда не состоял(а) в браке"
        или сообщению для несовершеннолетних, возвращает False и устанавливает
        соответствующее сообщение. В остальных случаях возвращает True.
        """
        if self._spouse_exists is not None:
            return self._spouse_exists
        if self._bio.age < self.AGE_MAJORITY:
            self._data.no_spouse_message = self.SMALL_AGE_ANSWERS[5]
            self._spouse_exists = False
            return False
        if self._bio.gender == self.GENDER[0]:
            if self.marital_status == self.MALE_MARITAL_STATUSES[0] or \
                    self.marital_status == self.SMALL_AGE_ANSWERS[5]:
                self._data.no_spouse_message = "У него нет жены, потому что не был в браке"
                self._spouse_exists = False
                return False
        else:
            if self.marital_status == self.FEMALE_MARITAL_STATUSES[0] or \
                    self.marital_status == self.SMALL_AGE_ANSWERS[5]:
                self._data.no_spouse_message = "У неё нет мужа, потому что не была в браке"
                self._spouse_exists = False
                return False

        self._spouse_exists = True
        return True

    def _generate_spouse_name_parts(self):
        """
        Суть: Генерация ФИО супруга. Использует вспомогательную функцию choice_machine_family
        для генерации фамилии, имени и отчества супруга в зависимости от пола человека и его
        семейного статуса. Сохраняет сгенерированные данные во внутреннем хранилище. Также
        сохраняет флаг о том, был ли супруг ранее в браке.
        """
        if self._data.spouse_surname is not None:
            return
        surname, was_married = choice_machine_family(
            value=self._data.spouse_surname,
            age=self._bio.age,
            gender=self._bio.gender,
            marital_status=self.marital_status,
            answer_1=self.SMALL_AGE_ANSWERS,
            gender_answer=self.GENDER,
            male_1=self.MALE_MARITAL_STATUSES,
            female_1=self.FEMALE_MARITAL_STATUSES,
            ml=self.MALE_SURNAMES,
            fml=self.FEMALE_SURNAMES
        )
        self._data.spouse_surname = surname
        self._data.spouse_was_married = was_married
        name, _ = choice_machine_family(
            value=self._data.spouse_name,
            age=self._bio.age,
            gender=self._bio.gender,
            marital_status=self.marital_status,
            answer_1=self.SMALL_AGE_ANSWERS,
            gender_answer=self.GENDER,
            male_1=self.MALE_MARITAL_STATUSES,
            female_1=self.FEMALE_MARITAL_STATUSES,
            ml=self.MALE_NAMES,
            fml=self.FEMALE_NAMES
        )
        self._data.spouse_name = name
        patronymic, _ = choice_machine_family(
            value=self._data.spouse_patronymic,
            age=self._bio.age,
            gender=self._bio.gender,
            marital_status=self.marital_status,
            answer_1=self.SMALL_AGE_ANSWERS,
            gender_answer=self.GENDER,
            male_1=self.MALE_MARITAL_STATUSES,
            female_1=self.FEMALE_MARITAL_STATUSES,
            ml=self.MALE_PATRONYMICS,
            fml=self.FEMALE_PATRONYMICS
        )
        self._data.spouse_patronymic = patronymic

    @property
    @handle_errors
    def marital_status(self) -> str:
        """
        Суть: Получение семейного статуса. Для несовершеннолетних (младше 18 лет)
        возвращает соответствующий ответ из SMALL_AGE_ANSWERS[5]. Для совершеннолетних
        выбирает случайный семейный статус из списка в зависимости от пола: для мужчин
        из MALE_MARITAL_STATUSES, для женщин из FEMALE_MARITAL_STATUSES. Результат
        сохраняется во внутреннем хранилище.
        """
        if self._data.marital_status is None:
            if self._bio.age < 18:
                self._data.marital_status = self.SMALL_AGE_ANSWERS[5]
            elif self._bio.gender == self.GENDER[0]:
                self._data.marital_status = random.choice(self.MALE_MARITAL_STATUSES)
            else:
                self._data.marital_status = random.choice(self.FEMALE_MARITAL_STATUSES)
        return self._data.marital_status

    @property
    @handle_errors
    @check_spouse(attr_name='spouse_surname')
    def spouse_surname(self) -> str:
        """
        Суть: Получение фамилии супруга. Использует декоратор check_spouse для
        проверки наличия супруга. При наличии супруга вызывает метод
        _generate_spouse_name_parts для генерации фамилии супруга. Результат
        сохраняется во внутреннем хранилище.
        """
        self._generate_spouse_name_parts()
        return self._data.spouse_surname

    @property
    @handle_errors
    @check_spouse(attr_name='spouse_name')
    def spouse_name(self) -> str:
        """
        Суть: Получение имени супруга. Использует декоратор check_spouse для проверки
        наличия супруга. При наличии супруга вызывает метод _generate_spouse_name_parts
        для генерации имени супруга. Результат сохраняется во внутреннем хранилище.
        """
        self._generate_spouse_name_parts()
        return self._data.spouse_name

    @property
    @handle_errors
    @check_spouse(attr_name='spouse_patronymic')
    def spouse_patronymic(self) -> str:
        """
        Суть: Получение отчества супруга. Использует декоратор check_spouse для проверки
        наличия супруга. Если супруг отсутствует, возвращает сообщение из no_spouse_message.
        При наличии супруга вызывает метод _generate_spouse_name_parts для генерации
        отчества супруга. Результат сохраняется во внутреннем хранилище.
        """
        if not self._check_spouse_exists():
            self._data.spouse_patronymic = self._data.no_spouse_message
            return self._data.spouse_patronymic
        self._generate_spouse_name_parts()
        return self._data.spouse_patronymic

    @property
    @handle_errors
    def spouse_full_name(self) -> str:
        """
        Суть: Получение полного ФИО супруга. Если супруг отсутствует, возвращает
        сообщение из no_spouse_message. При наличии супруга формирует строку в формате
        "Фамилия Имя Отчество". Если супруг ранее состоял в браке
        (spouse_was_married = True), добавляет суффикс "(была)" для мужчин или
        "(был)" для женщин. Результат сохраняется во внутреннем хранилище.
        """
        if not self._check_spouse_exists():
            return self._data.no_spouse_message
        self._generate_spouse_name_parts()
        full_name = f"{self._data.spouse_surname} {self._data.spouse_name} {self._data.spouse_patronymic}"
        if self._data.spouse_was_married:
            suffix = " (была)" if self._bio.gender == self.GENDER[0] else " (был)"
            full_name += suffix
        return full_name

    @property
    @handle_errors
    @check_spouse(attr_name='spouse_age')
    def spouse_age(self) -> int | str:
        """
        Суть: Получение возраста супруга. Генерирует возраст супруга на основе
        возраста человека. С вероятностью 1/3 возраст совпадает с возрастом человека.
        С вероятностью 1/3 возраст отличается на небольшую величину (до 8 лет в
        зависимости от возраста). С вероятностью 1/3 возраст может быть значительно
        больше или меньше (в пределах от AGE_MAJORITY до 105). Результат сохраняется
        во внутреннем хранилище.
        """
        if self._data.spouse_age is None:
            answer = random.randint(1, 3)
            if answer == 1:
                self._data.spouse_age = self._bio.age
            elif answer == 2:
                if self._bio.age == self.AGE_MAJORITY:
                    self._data.spouse_age = self.AGE_MAJORITY
                else:
                    answer_1 = self._bio.age - self.AGE_MAJORITY
                    rand_an = random.randint(1, answer_1)
                    if answer_1 < 8:
                        if random.choice([True, False]):
                            self._data.spouse_age = random.randint(self._bio.age, self._bio.age + rand_an)
                        else:
                            self._data.spouse_age = random.randint(self._bio.age - rand_an, self._bio.age)
                    elif answer_1 >= 8:
                        if random.choice([True, False]):
                            self._data.spouse_age = random.randint(self._bio.age, self._bio.age + 8)
                        else:
                            self._data.spouse_age = random.randint(self._bio.age - 8, self._bio.age)
            elif answer == 3:
                if random.choice([True, False]):
                    self._data.spouse_age = random.randint(self._bio.age, 105)
                else:
                    self._data.spouse_age = random.randint(self.AGE_MAJORITY, self._bio.age)
        return self._data.spouse_age

    @property
    @handle_errors
    @check_spouse(attr_name='marriage_date')
    def marriage_date(self) -> str:
        """
        Суть: Получение даты бракосочетания. Генерирует дату в формате "ДД.ММ.ГГГГ".
        Год выбирается случайно в диапазоне от (год рождения + AGE_MAJORITY) до
        текущего года. С вероятностью 50% день и месяц совпадают с днем и месяцем
        рождения человека, иначе генерируются случайные день (1-28) и месяц (от
        месяца рождения до 12). Результат сохраняется во внутреннем хранилище.
        """
        if self._data.marriage_date is None:
            answer = [int(x) for x in self._bio.year.split(".")]
            current_year = datetime.now().year
            min_year = answer[2] + self.AGE_MAJORITY
            max_year = current_year
            if min_year > max_year:
                year_start = min_year
            else:
                year_start = random.randint(min_year, max_year)
            short_1 = year_start % 100
            if random.choice([True, False]):
                self._data.marriage_date = f"{answer[0]:02d}.{answer[1]:02d}.{year_start}"
            else:
                day = random.randint(1, 28)
                month = random.randint(answer[1], 12)
                self._data.marriage_date = f"{day:02d}.{month:02d}.{year_start}"
        return self._data.marriage_date

    @property
    @handle_errors
    @check_spouse(attr_name='years_marriage')
    def years_marriage(self) -> int | str:
        """
        Суть: Получение количества лет в браке. Рассчитывает разницу между текущим
        годом и годом бракосочетания. Если месяц бракосочетания позже текущего месяца,
        вычитает 1 год. Результат сохраняется во внутреннем хранилище.
        """
        if self._data.years_marriage is None:
            year_mar = self.marriage_date.split(".")
            year_now = datetime.now().year
            answer = year_now - int(year_mar[2])
            if int(year_mar[1]) < datetime.now().month:
                answer -= 1
            self._data.years_marriage = answer
        return self._data.years_marriage

    @property
    @handle_errors
    @check_spouse(attr_name='children_count')
    def children_count(self) -> int | str:
        """
        Суть: Получение количества детей. С вероятностью 50% возвращает 0 или 1. В
        остальных случаях определяет количество детей в зависимости от стажа брака:
        при стаже 1-5 лет - от 1 до 3 детей, при стаже 6-15 лет - от 4 до 6 детей,
        при стаже более 15 лет - от 1 до 10 детей. Результат сохраняется во
        внутреннем хранилище.
        """
        if self._data.children_count is None:
            if random.choice([True, False]):
                if random.choice([True, False]):
                    self._data.children_count = 0
                else:
                    self._data.children_count = 1
            else:
                if 1 <= self._data.years_marriage <= 5:
                    self._data.children_count = random.randint(1, 3)
                elif 6 <= self._data.years_marriage <= 15:
                    self._data.children_count = random.randint(4, 6)
                else:
                    self._data.children_count = random.randint(1, 10)
        return self._data.children_count

    @handle_errors
    @check_spouse(attr_name='children_names')
    def children_names(self, visualization: bool = False) -> List[str] | str:
        """
        Суть: Получение списка имен детей. Если детей нет, возвращает "Нет детей".
        Для каждого ребенка случайным образом выбирает имя из списка мужских или
        женских имен. Если параметр visualization=True, возвращает строку с именами
        через запятую, иначе возвращает список. Результат сохраняется во
        внутреннем хранилище.
        """
        if self._data.children_names is None:
            if self._data.children_count == 0:
                self._data.children_names = "Нет детей"
                return self._data.children_names
            lst_names = []
            for name in range(self._data.children_count):
                name_list = random.choice([self.FEMALE_NAMES, self.MALE_NAMES])
                lst_names.append(random.choice(name_list))
            self._data.children_names = lst_names
        if visualization:
            return ", ".join(self._data.children_names)
        return self._data.children_names

    @property
    @handle_errors
    def living_with_parents(self) -> bool:
        """
        Суть: Получение статуса проживания с родителями. Если выполняются условия
        (возраст меньше 40 лет, зарплата ниже 65000 рублей, отсутствие супруга),
        с вероятностью 50% возвращает True. В остальных случаях возвращает False.
        Результат сохраняется во внутреннем хранилище.
        """
        if self._data.living_with_parents is None:
            if any([self._bio.age < 40,
                    self._finance.salary < 65000,
                    not self._check_spouse_exists()]):
                if random.choice([True, False]):
                    self._data.living_with_parents = True
                else:
                    self._data.living_with_parents = False
            else:
                self._data.living_with_parents = False
        return self._data.living_with_parents

    @property
    @handle_errors
    @check_spouse(attr_name='family_members_count')
    def family_members_count(self) -> int | str:
        """
        Суть: Получение количества членов семьи. Рассчитывает как количество детей
        + 2 (человек и супруг). Если семейный статус соответствует "Разведен(а)",
        вычитает 1 (супруг отсутствует). Результат сохраняется во внутреннем хранилище.
        """
        if self._data.family_members_count is None:
            answer = self.children_count + 2
            if self.marital_status == self.MALE_MARITAL_STATUSES[3] or \
                self.marital_status == self.FEMALE_MARITAL_STATUSES[3]:
                answer -= 1
            self._data.family_members_count = answer
        return self._data.family_members_count

    def __str__(self) -> str:
        """
        Суть: Строковое представление всех сгенерированных семейных данных.
        Формирует многострочную строку, содержащую все семейные компоненты:
        семейный статус, ФИО супруга, возраст супруга, дата бракосочетания,
        количество лет в браке, количество детей, имена детей, проживание с
        родителями, количество членов семьи. Используется для удобного вывода
        всей информации о сгенерированных семейных данных.
        """
        return (f"Семейный статус: {self.marital_status}\n"
                f"ФИО супруга: {self.spouse_full_name}\n"
                f"Возраст супруга: {self.spouse_age}\n"
                f"Дата бракосочетания: {self.marriage_date}\n"
                f"Лет в браке: {self.years_marriage}\n"
                f"Количество детей: {self.children_count}\n"
                f"Имена детей: {self.children_names()}\n"
                f"Живёт ли с родителями: {self.living_with_parents}\n"
                f"Количество членов семьи: {self.family_members_count}\n")