import random
from typing import List
from datetime import datetime, timedelta
from dataclasses import dataclass
from .b_h__base_generator import BaseGenerator
from FakerRussia.b__additional_algorithms.a_a__handle_errors import handle_errors


@dataclass
class _WorkData:
    """
    Суть: Внутренний контейнер данных для хранения состояния генератора рабочих данных.
    Хранит сгенерированные рабочие компоненты (должность, трудовой стаж, уровень работы,
    место работы, заболевания, вредные привычки, хобби, уровень английского языка, дата
    начала работы, рабочий график, статус трудоустройства) для обеспечения согласованности
    данных при множественных обращениях к свойствам.
    """
    job: str = None
    work_experience: str = None
    level_work: str = None
    place_work: str = None
    diseases: List[str] | str = None
    bad_habits: List[str] | str = None
    hobby: List[str] | str = None
    english_level: str = None
    job_start_date: str = None
    work_schedule: str = None
    is_employed: bool = None


class WorkGenerator(BaseGenerator):
    """
    Суть: Генератор рабочих данных человека. Предоставляет функциональность для генерации
    различных рабочих характеристик: должность и статус занятости, трудовой стаж, уровень
    квалификации, место работы, список заболеваний (на основе военной категории), вредные
    привычки, хобби (в зависимости от возраста), уровень владения английским языком, дата
    начала работы, рабочий график. Данные загружаются из JSON-файлов. Для генерации использует
    информацию из переданного генератора биографии.
    """

    def __init__(self, bio):
        """
        Суть: Инициализация генератора рабочих данных. Создает экземпляр генератора,
        сохраняет ссылку на генератор биографии (bio) для использования его данных.
        Инициализирует внутреннее хранилище данных _WorkData и загружает рабочие данные
        из JSON-файлов через метод _load_work_data.
        """
        super().__init__()
        self._bio = bio
        self._data = _WorkData()
        self._load_work_data()

    def _load_work_data(self):
        """
        Суть: Загрузка рабочих данных из JSON-файлов. Загружает список профессий и
        должностей из файла 'a__data/job/jobs.json', статусы занятости (безработный,
        самозанятый и т.д.) из файла 'a__data/job/employment_status.json', типы
        бизнеса из файла 'a__data/business_type/business_types.json', названия компаний
        из файла 'a__data/company_name/company_names.json', список заболеваний
        (с группировкой по военным категориям) из файла 'a__data/disease/diseases.json',
        список серьезных вредных привычек из файла 'a__data/bad_habits/bad_habits.json',
        список хобби (с разбивкой по возрастным группам) из файла 'a__data/hobby/hobbies.json',
        уровни английского языка из файла 'a__data/english_level/english_levels.json',
        графики работы из файла 'a__data/work_schedule/work_schedules.json'. Сохраняет
        загруженные данные в атрибуты класса для дальнейшего использования.
        """
        jobs_data = self._load_json('a__data/job/jobs.json')
        self.JOBS = jobs_data.get("JOBS", {})
        employment_status_data = self._load_json('a__data/job/employment_status.json')
        self.EMPLOYMENT_STATUS = employment_status_data.get("EMPLOYMENT_STATUS", [])
        business_types_data = self._load_json('a__data/business_type/business_types.json')
        self.BUSINESS_TYPES = business_types_data.get("BUSINESS_TYPES", [])
        company_names_data = self._load_json('a__data/company_name/company_names.json')
        self.COMPANY_NAMES = company_names_data.get("COMPANY_NAMES", [])
        diseases_data = self._load_json('a__data/disease/diseases.json')
        self.DISEASES = diseases_data.get("DISEASES", [])
        bad_habits_data = self._load_json('a__data/bad_habits/bad_habits.json')
        self.SERIOUS_BAD_HABITS = bad_habits_data.get("SERIOUS_BAD_HABITS", [])
        hobbies_data = self._load_json('a__data/hobby/hobbies.json')
        self.HOBBIES = hobbies_data.get("HOBBIES", {})
        english_levels_data = self._load_json('a__data/english_level/english_levels.json')
        self.ENGLISH_LEVELS = english_levels_data.get("ENGLISH_LEVELS", [])
        work_schedules_data = self._load_json('a__data/work_schedule/work_schedules.json')
        self.WORK_SCHEDULES = work_schedules_data.get("WORK_SCHEDULES", [])

    def reset(self):
        """
        Суть: Сброс сгенерированных рабочих данных. Очищает внутреннее хранилище данных,
        создавая новый экземпляр _WorkData, что позволяет сгенерировать новый набор рабочих
        компонентов при последующих обращениях к свойствам.
        """
        self._data = _WorkData()
        return "Рабочие данные сброшены"

    @property
    @handle_errors
    def job(self) -> str:
        """
        Суть: Получение должности или статуса занятости. Для несовершеннолетних (младше AGE_MAJORITY)
        возвращает соответствующий ответ из SMALL_AGE_ANSWERS[0]. Для пенсионеров (мужчины 64+,
        женщины 59+) возвращает значение PENSION. Для остальных с вероятностью 50% выбирает
        случайную профессию из списка JOBS, иначе выбирает случайный статус занятости из списка
        EMPLOYMENT_STATUS. Результат сохраняется во внутреннем хранилище.
        """
        if self._data.job is None:
            if self._bio.age < self.AGE_MAJORITY:
                self._data.job = self.SMALL_AGE_ANSWERS[0]
            elif ((self._bio.gender == self.GENDER[0] and self._bio.age >= 64) or
                  (self._bio.gender == self.GENDER[1] and self._bio.age >= 59)):
                self._data.job = self.PENSION
            elif random.choice([True, False]):
                self._data.job = random.choice(list(self.JOBS.keys()))
            else:
                self._data.job = random.choice(self.EMPLOYMENT_STATUS)
        return self._data.job

    @property
    @handle_errors
    def work_experience(self) -> str:
        """
        Суть: Получение трудового стажа в годах. Для несовершеннолетних (младше AGE_MAJORITY)
        возвращает соответствующий ответ из SMALL_AGE_ANSWERS[0]. Для остальных рассчитывает
        стаж как разницу между текущим возрастом и возрастом начала трудовой деятельности
        (AGE_MAJORITY). Если человек достиг пенсионного возраста, стаж считается до момента
        выхода на пенсию (64 года для мужчин, 59 лет для женщин). Результат сохраняется во
        внутреннем хранилище.
        """
        if self._data.work_experience is None:
            if self._bio.age < self.AGE_MAJORITY:
                self._data.work_experience = self.SMALL_AGE_ANSWERS[0]
            else:
                retirement = 64 if self._bio.gender == self.GENDER[0] else 59
                if self._bio.age <= retirement:
                    years = self._bio.age - self.AGE_MAJORITY
                else:
                    years = retirement - self.AGE_MAJORITY
                self._data.work_experience = str(max(0, years))
        return self._data.work_experience

    @property
    @handle_errors
    def level_work(self) -> str:
        """
        Суть: Получение уровня квалификации/опыта работы. Если должность равна PENSION,
        возвращает PENSION. Для остальных определяет уровень работы на основе трудового
        стажа: 0 лет - стажер/без опыта, 1-2 года - начинающий специалист, 3-5 лет -
        младший специалист, 6-9 лет - специалист, 10-12 лет - ведущий специалист, более
        12 лет - эксперт. Уровни берутся из списка LEVEL_WORK. Результат сохраняется во
        внутреннем хранилище.
        """
        if self._data.level_work is None:
            if self._data.job == self.PENSION:
                self._data.level_work = self.PENSION
                return self._data.level_work
            exp = 0
            try:
                exp = int(self.work_experience)
            except:
                exp = 0
            if exp == 0:
                self._data.level_work = self.LEVEL_WORK[0]
            elif 0 < exp <= 2:
                self._data.level_work = self.LEVEL_WORK[1]
            elif 2 < exp <= 5:
                self._data.level_work = self.LEVEL_WORK[2]
            elif 5 < exp <= 9:
                self._data.level_work = self.LEVEL_WORK[3]
            elif 9 < exp <= 12:
                self._data.level_work = self.LEVEL_WORK[4]
            else:
                self._data.level_work = self.LEVEL_WORK[5]
        return self._data.level_work

    @property
    @handle_errors
    def place_work(self) -> str:
        """
        Суть: Получение места работы (названия организации). Если должность равна PENSION,
        возвращает PENSION. Для несовершеннолетних возвращает "Места работы нет". Для
        остальных с вероятностью 50% формирует название ИП в формате "ИП Фамилия Имя
        Отчество" (имя, фамилия и отчество выбираются случайно из мужских или женских
        списков), иначе формирует название организации в формате "Тип бизнеса 'Название
        компании'". Результат сохраняется во внутреннем хранилище.
        """
        if self._data.place_work is None:
            if self._data.job == self.PENSION:
                self._data.place_work = self.PENSION
                return self._data.place_work
            if self._bio.age < self.AGE_MAJORITY:
                self._data.place_work = "Места работы нет"
            elif random.choice([True, False]):
                if random.choice([True, False]):
                    first_name = random.choice(self._bio.MALE_NAMES)
                    last_name = random.choice(self._bio.MALE_SURNAMES)
                    patronymic = random.choice(list(self._bio.MALE_PATRONYMICS.keys()))
                else:
                    first_name = random.choice(self._bio.FEMALE_NAMES)
                    last_name = random.choice(self._bio.FEMALE_SURNAMES)
                    patronymic = random.choice(list(self._bio.FEMALE_PATRONYMICS.keys()))
                self._data.place_work = f"ИП {last_name} {first_name} {patronymic}"
            else:
                self._data.place_work = f"{random.choice(self.BUSINESS_TYPES)} '{random.choice(self.COMPANY_NAMES)}'"
        return self._data.place_work

    @handle_errors
    def diseases(self, visualization: bool = False) -> List[str] | str:
        """
        Суть: Получение списка заболеваний. Генерирует список из 1-4 случайных заболеваний.
        Заболевания выбираются из словаря DISEASES по ключу, соответствующему военной
        категории годности человека (self._bio.military_fitness_category). Если параметр
        visualization=True, возвращает строку с элементами через запятую, иначе возвращает
        список. Результат сохраняется во внутреннем хранилище.
        """
        if self._data.diseases is None:
            if self._bio.military_fitness_category == "A1":
                self._data.diseases = random.choice(self.DISEASES[self._bio.military_fitness_category])
            lst_diseases = []
            for dis in range(random.randint(1, 4)):
                lst_diseases.append(random.choice(self.DISEASES[self._bio.military_fitness_category]))
            self._data.diseases = lst_diseases
        if visualization:
            return ", ".join(self._data.diseases)
        return self._data.diseases

    @handle_errors
    def bad_habits(self, visualization: bool = False) -> List[str] | str:
        """
        Суть: Получение списка вредных привычек. Для детей младше 10 лет возвращает соответствующий
        ответ из SMALL_AGE_ANSWERS[1]. Для остальных с вероятностью 50% генерирует список из 1-5
        случайных вредных привычек из списка SERIOUS_BAD_HABITS, иначе возвращает "У данного
        человека не обнаружено вредных привычек". Если параметр visualization=True, возвращает
        строку с элементами через запятую, иначе возвращает список. Результат сохраняется во
        внутреннем хранилище.
        """
        if self._data.bad_habits is None:
            if self._bio.age < 10:
                self._data.bad_habits = self.SMALL_AGE_ANSWERS[1]
            elif random.choice([True, False]):
                selected = [random.choice(self.SERIOUS_BAD_HABITS) for _ in range(random.randint(1, 5))]
                self._data.bad_habits = selected
            else:
                self._data.bad_habits = "У данного человека не обнаружено вредных привычек"
        if visualization:
            return ", ".join(self._data.bad_habits)
        return self._data.bad_habits

    @handle_errors
    def hobby(self, visualization: bool = False) -> List[str] | str:
        """
        Суть: Получение списка хобби. Для детей младше 4 лет возвращает соответствующий ответ
        из SMALL_AGE_ANSWERS[2]. Для остальных определяет возрастную группу человека по
        диапазонам из словаря HOBBIES и выбирает случайное количество хобби (от 1 до 5) из
        списка, соответствующего этой возрастной группе. Если параметр visualization=True,
        возвращает строку с элементами через запятую, иначе возвращает список. Результат
        сохраняется во внутреннем хранилище.
        """
        if self._data.hobby is None:
            if self._bio.age < 4:
                self._data.hobby = self.SMALL_AGE_ANSWERS[2]
            else:
                lst_answer = []
                for key, value in self.HOBBIES.items():
                    age = [int(x) for x in key.split("-")]
                    if age[0] <= self._bio.age <= age[1]:
                        rand_num = random.randint(1, 5)
                        for _ in range(rand_num):
                            lst_answer.append(random.choice(value))
                self._data.hobby = lst_answer
        if visualization:
            return ", ".join(self._data.hobby)
        return self._data.hobby

    @property
    @handle_errors
    def english_level(self) -> str:
        """
        Суть: Получение уровня владения английским языком. Возвращает случайный уровень
        английского языка из загруженного списка ENGLISH_LEVELS. Результат сохраняется
        во внутреннем хранилище.
        """
        if self._data.english_level is None:
            self._data.english_level = random.choice(self.ENGLISH_LEVELS)
        return self._data.english_level

    @property
    @handle_errors
    def job_start_date(self) -> str:
        """
        Суть: Получение даты начала работы. Для несовершеннолетних возвращает "Не работает".
        Для остальных рассчитывает дату начала работы как текущая дата минус количество
        лет стажа (work_experience). Если рассчитанная дата раньше даты достижения 18-летия,
        дата начала работы устанавливается на дату 18-летия. Формат: "ДД.ММ.ГГГГ".
        Результат сохраняется во внутреннем хранилище.
        """
        if self._data.job_start_date is None:
            if self._bio.age < self.AGE_MAJORITY:
                self._data.job_start_date = "Не работает"
            else:
                exp = int(self.work_experience)
                now = datetime.now()
                start_date = now - timedelta(days=exp * 365)
                birth_day, birth_month, birth_year = map(int, self._bio.year.split('.'))
                eighteen_date = datetime(birth_year + 18, birth_month, birth_day)
                if start_date < eighteen_date:
                    start_date = eighteen_date
                self._data.job_start_date = start_date.strftime("%d.%m.%Y")
        return self._data.job_start_date

    @property
    @handle_errors
    def work_schedule(self) -> str:
        """
        Суть: Получение рабочего графика. Если должность равна PENSION, возвращает PENSION.
        Для несовершеннолетних возвращает "Не работает". Для остальных возвращает случайный
        график работы из списка WORK_SCHEDULES. Результат сохраняется во внутреннем хранилище.
        """
        if self._data.work_schedule is None:
            if self._data.job == self.PENSION:
                self._data.work_schedule = self.PENSION
                return self._data.work_schedule
            if self._bio.age < self.AGE_MAJORITY:
                self._data.work_schedule = "Не работает"
                return self._data.work_schedule
            self._data.work_schedule = random.choice(self.WORK_SCHEDULES)
        return self._data.work_schedule

    @property
    def is_employed(self) -> bool:
        """
        Суть: Получение статуса трудоустройства. Возвращает True, если должность человека не
        входит в список статусов занятости (EMPLOYMENT_STATUS), не является пенсионером
        (PENSION) и не является несовершеннолетним (SMALL_AGE_ANSWERS). В противном случае
        возвращает False. Результат сохраняется во внутреннем хранилище.
        """
        if self._data.is_employed is None:
            self._data.is_employed = (self.job not in self.EMPLOYMENT_STATUS and
                                        self.job != self.PENSION and
                                        self.job not in self.SMALL_AGE_ANSWERS)
        return self._data.is_employed

    def __str__(self) -> str:
        """
        Суть: Строковое представление всех сгенерированных рабочих данных. Формирует многострочную
        строку, содержащую все рабочие компоненты: статус трудоустройства, должность, трудовой
        стаж, дата начала работы, уровень квалификации, место работы, список заболеваний, вредные
        привычки, хобби, уровень английского языка, рабочий график. Используется для удобного
        вывода всей информации о сгенерированных рабочих данных.
        """
        return (f"Работает ли человек: {self.is_employed}\n"
                f"Работа: {self.job}\n"
                f"Стаж работы: {self.work_experience}\n"
                f"Дата начала работы: {self.job_start_date}\n"
                f"Уровень работы: {self.level_work}\n"
                f"Место работы: {self.place_work}\n"
                f"Болезни: {self.diseases()}\n"
                f"Вредные привычки: {self.bad_habits()}\n"
                f"Хобби: {self.hobby()}\n"
                f"Уровень английского языка: {self.english_level}\n"
                f"Рабочий график: {self.work_schedule}")