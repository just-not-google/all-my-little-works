import random
from typing import List
from dataclasses import dataclass
from .b_h__base_generator import BaseGenerator
from FakerRussia.b__additional_algorithms.a_a__handle_errors import handle_errors


@dataclass
class _DocumentData:
    """
    Суть: Внутренний контейнер данных для хранения состояния генератора документальных данных.
    Хранит сгенерированные документальные компоненты (ИНН, СНИЛС, серия и номер паспорта,
    дата выдачи паспорта, код подразделения, ЕНП, административные нарушения) для обеспечения
    согласованности данных при множественных обращениях к свойствам.
    """
    inn: str = None
    snils: str = None
    passport_series_number: str = None
    date_issue: str = None
    unit_code: str = None
    enp: str = None
    administrative_violations: List[str] | str = None


class DocumentGenerator(BaseGenerator):
    """
    Суть: Генератор документальных данных человека. Предоставляет функциональность для
    генерации различных документов и их реквизитов: ИНН (индивидуальный номер налогоплательщика)
    с корректной контрольной суммой, СНИЛС (страховой номер индивидуального лицевого счета) с
    контрольным числом, серия и номер паспорта (с кодом региона по месту жительства), дата
    выдачи паспорта (в зависимости от возраста), код подразделения, выдавшего паспорт, ЕНП
    (единый номер полиса ОМС), список административных нарушений (ПДД и другие). Данные
    загружаются из JSON-файлов. Для генерации использует информацию из переданных генераторов
    биографии, адреса и автомобиля.
    """

    def __init__(self, bio, address, car):
        """
        Суть: Инициализация генератора документальных данных. Создает экземпляр генератора,
        сохраняет ссылки на генераторы биографии (bio), адреса (address) и автомобиля (car)
        для использования их данных. Инициализирует внутреннее хранилище данных _DocumentData
        и загружает документальные данные из JSON-файлов через метод _load_document_data.
        """
        super().__init__()
        self._bio = bio
        self._address = address
        self._car = car
        self._data = _DocumentData()
        self._load_document_data()

    def _load_document_data(self):
        """
        Суть: Загрузка документальных данных из JSON-файлов. Загружает коды регионов для паспортов
        из файла 'a__data/passport/regions_codes.json', префиксы ИНН по городам из файла
        'a__data/inn/region_codes.json', списки административных нарушений (не связанных с ПДД)
        из файла 'a__data/administrative_violations/administrative_violations_other.json', списки
        нарушений ПДД из файла 'a__data/administrative_violations/administrative_violations_pdd.json'.
        Сохраняет загруженные данные в атрибуты класса для дальнейшего использования.
        """
        passport_data = self._load_json('a__data/passport/regions_codes.json')
        self.PASSPORT_REGION_CODES = passport_data.get("PASSPORT_REGION_CODES", {})
        inn_data = self._load_json('a__data/inn/region_codes.json')
        self.CITY_TO_INN_PREFIX = inn_data.get("CITY_TO_INN_PREFIX", {})
        administrative_violations_other_data = self._load_json('a__data/administrative_violations/administrative_violations_other.json')
        self.ADMIN_VIOLATIONS_OTHER = administrative_violations_other_data.get("ADMIN_VIOLATIONS_OTHER", [])
        administrative_violations_pdd_data = self._load_json('a__data/administrative_violations/administrative_violations_pdd.json')
        self.ADMIN_VIOLATIONS_TRAFFIC = administrative_violations_pdd_data.get("ADMIN_VIOLATIONS_TRAFFIC", [])

    def reset(self):
        """
        Суть: Сброс сгенерированных документальных данных. Очищает внутреннее хранилище данных,
        создавая новый экземпляр _DocumentData, что позволяет сгенерировать новый набор
        документальных компонентов при последующих обращениях к свойствам.
        """
        self._data = _DocumentData()
        return "Документальные данные сброшены"

    @property
    @handle_errors
    def inn(self):
        """
        Суть: Получение ИНН (индивидуального номера налогоплательщика). Генерирует 12-значный
        ИНН с корректными контрольными суммами. Первые 4 цифры - префикс региона из CITY_TO_INN_PREFIX
        по городу. Следующие 6 цифр - случайное число от 0 до 999999 с ведущими нулями. 11-я цифра
        вычисляется как сумма произведений первых 10 цифр на весовые коэффициенты WEIGHT_FACTORS_1,
        затем остаток от деления на 11 (если >9, берется последняя цифра). 12-я цифра вычисляется
        аналогично с использованием WEIGHT_FACTORS_2. Результат сохраняется во внутреннем хранилище.
        """
        if self._data.inn is None:
            first_4 = self.CITY_TO_INN_PREFIX[self._address.city]
            second_6 = str(random.randint(0, 999999)).zfill(6)
            digits = [int(d) for d in first_4 + second_6]
            sum11 = sum(digits[i] * self.WEIGHT_FACTORS_1[i] for i in range(10))
            digit11 = sum11 % 11
            if digit11 > 9:
                digit11 %= 10
            digits.append(digit11)
            sum12 = sum(digits[i] * self.WEIGHT_FACTORS_2[i] for i in range(11))
            digit12 = sum12 % 11
            if digit12 > 9:
                digit12 %= 10
            self._data.inn = f"{first_4}{second_6}{digit11}{digit12}"
        return self._data.inn

    @property
    @handle_errors
    def snils(self):
        """
        Суть: Получение СНИЛС (страхового номера индивидуального лицевого счета). Генерирует
        11-значный номер в формате "XXX-XXX-XXX YY". Первые 9 цифр - случайное число от
        100000000 до 999999999. Контрольное число вычисляется как сумма произведений каждой
        цифры на (9 - позиция), затем остаток от деления на 101. Если остаток равен 100,
        контрольное число становится 0. Результат сохраняется во внутреннем хранилище.
        """
        if self._data.snils is None:
            num = random.randint(100000000, 999999999)
            digits = [int(d) for d in str(num)]
            total = sum((9 - i) * digits[i] for i in range(9))
            control = total % 101
            if control == 100:
                control = 0
            self._data.snils = f"{str(num)[:3]}-{str(num)[3:6]}-{str(num)[6:9]} {control:02d}"
        return self._data.snils

    @property
    @handle_errors
    def passport_series_number(self):
        """
        Суть: Получение серии и номера паспорта. Для детей младше 14 лет возвращает
        соответствующий ответ из SMALL_AGE_ANSWERS[8]. Для остальных формирует серию и
        номер паспорта в формате "XX XX XXXXXX". Первые две цифры - код региона из PASSPORT_REGION_CODES
        по городу (если город не найден, используется "00"). Следующие две цифры -
        случайное число от 1 до 96 с ведущим нулем. Последние 6 цифр - случайное число от 100000
        до 999999. Результат сохраняется во внутреннем хранилище.
        """
        if self._data.passport_series_number is None:
            if self._bio.age < 14:
                self._data.passport_series_number = self.SMALL_AGE_ANSWERS[8]
            else:
                try:
                    first_2 = self.PASSPORT_REGION_CODES[self._address.city]
                except KeyError:
                    first_2 = "00"
                second_2 = f"{random.randint(1, 96):02d}"
                third_6 = random.randint(100000, 999999)
                self._data.passport_series_number = f"{first_2} {second_2} {third_6}"
        return self._data.passport_series_number

    @property
    @handle_errors
    def date_issue(self):
        """
        Суть: Получение даты выдачи паспорта. Для детей младше 14 лет возвращает соответствующий
        ответ из SMALL_AGE_ANSWERS[8]. Для остальных рассчитывает дату выдачи на основе возраста:
        для граждан 14-19 лет паспорт выдается в 14 лет, для граждан 20-44 лет - в 20 лет, для
        граждан 45 лет и старше - в 45 лет. Дата выдачи совпадает с днем и месяцем рождения.
        Формат: "ДД.ММ.ГГГГ". Результат сохраняется во внутреннем хранилище.
        """
        if self._data.date_issue is None:
            if self._bio.age < 14:
                self._data.date_issue = self.SMALL_AGE_ANSWERS[8]
            else:
                birth = self._bio.year.split(".")
                birth_year = int(birth[2])
                birth_month = int(birth[1])
                birth_day = int(birth[0])
                if 14 <= self._bio.age < 20:
                    issue_year = birth_year + 14
                elif 20 <= self._bio.age < 45:
                    issue_year = birth_year + 20
                else:
                    issue_year = birth_year + 45
                self._data.date_issue = f"{birth_day:02d}.{birth_month:02d}.{issue_year}"
        return self._data.date_issue

    @property
    @handle_errors
    def unit_code(self):
        """
        Суть: Получение кода подразделения, выдавшего паспорт. Для детей младше 14 лет
        возвращает соответствующий ответ из SMALL_AGE_ANSWERS[8]. Для остальных формирует
        код подразделения. Первая часть - код региона из PASSPORT_REGION_CODES по городу
        (если не найден, используется "00") плюс 4 случайные цифры от 1000 до 9999. Затем
        код переворачивается: вторая половина становится первой, первая половина - второй,
        разделенные дефисом. Формат: "XXXX-XXXX". Результат сохраняется во внутреннем хранилище.
        """
        if self._data.unit_code is None:
            if self._bio.age < 14:
                self._data.unit_code = self.SMALL_AGE_ANSWERS[8]
            else:
                code = f"{self.PASSPORT_REGION_CODES.get(self._address.city, '00')}{random.randint(1000, 9999)}"
                mid = len(code) // 2
                self._data.unit_code = f"{code[mid:]}-{code[:mid]}"
        return self._data.unit_code

    @property
    @handle_errors
    def enp(self):
        """
        Суть: Получение ЕНП (единого номера полиса ОМС). Генерирует 16-значный номер с
        контрольной суммой по алгоритму Луна. Первая цифра всегда 2. Следующие 2 цифры
        - код региона из PASSPORT_REGION_CODES (с ведущим нулем, если необходимо). Затем
        12 случайных цифр. Контрольная сумма вычисляется по алгоритму: цифры на нечетных
        позициях (с конца) удваиваются, если результат больше 9, вычитается 9, затем все
        суммируется, контрольная цифра = (10 - (сумма % 10)) % 10. Результат сохраняется
        во внутреннем хранилище.
        """
        if self._data.enp is None:
            region = self.PASSPORT_REGION_CODES.get(self._address.city, "00")
            unique = [random.randint(0, 9) for _ in range(12)]
            digits = [2] + [int(d) for d in str(region).zfill(2)] + unique
            temp = digits.copy()
            for i in range(len(temp) - 1, -1, -2):
                temp[i] *= 2
                if temp[i] > 9:
                    temp[i] -= 9
            checksum = (10 - (sum(temp) % 10)) % 10
            self._data.enp = ''.join(map(str, digits + [checksum]))
        return self._data.enp

    @handle_errors
    def administrative_violations(self, visualization: bool = False) -> List[str] | str:
        """
        Суть: Получение списка административных нарушений. Для детей младше 16 лет возвращает
        соответствующий ответ из SMALL_AGE_ANSWERS[13]. С вероятностью 30% возвращает "У данного
        человека нет административных нарушений". В остальных случаях генерирует список из 1-4
        случайных нарушений. Если у человека есть автомобиль (self._car.has_car), нарушения
        могут быть как из списка ADMIN_VIOLATIONS_OTHER, так и из списка ADMIN_VIOLATIONS_TRAFFIC
        (нарушения ПДД). Если автомобиля нет, нарушения берутся только из ADMIN_VIOLATIONS_OTHER.
        Если параметр visualization=True, возвращает строку с элементами через запятую, иначе возвращает список.
        """
        if self._data.administrative_violations is None:
            if self._bio.age < 16:
                self._data.administrative_violations = self.SMALL_AGE_ANSWERS[13]
            else:
                if random.random() < 0.3:
                    self._data.administrative_violations = "У данного человека нет административных нарушений"
                else:
                    if self._car.has_car:
                        comb_lst = self.ADMIN_VIOLATIONS_OTHER + self.ADMIN_VIOLATIONS_TRAFFIC
                        self._data.administrative_violations = [random.choice(comb_lst) for _ in
                                                                range(random.randint(1, 4))]
                    else:
                        self._data.administrative_violations = [random.choice(self.ADMIN_VIOLATIONS_OTHER) for _ in
                                                                range(random.randint(1, 4))]
        if visualization:
            return ", ".join(self._data.administrative_violations)
        return self._data.administrative_violations

    def __str__(self):
        """
        Суть: Строковое представление всех сгенерированных документальных данных. Формирует
        многострочную строку, содержащую все документальные компоненты: ИНН, СНИЛС, серия и
        номер паспорта, дата выдачи паспорта, код подразделения, ЕНП, административные нарушения.
        Используется для удобного вывода всей информации о сгенерированных документальных данных.
        """
        return (f"ИНН: {self.inn}\n"
                f"СНИЛС: {self.snils}\n"
                f"Паспорт: {self.passport_series_number}\n"
                f"Дата выдачи паспорта: {self.date_issue}\n"
                f"Код подразделения паспорта: {self.unit_code}\n"
                f"ЕНП: {self.enp}\n"
                f"Административные нарушения: {self.administrative_violations()}")