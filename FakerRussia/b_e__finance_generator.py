import random
from typing import List
from datetime import datetime
from dataclasses import dataclass
from .b_h__base_generator import BaseGenerator
from FakerRussia.b__additional_algorithms.a_a__handle_errors import handle_errors
from FakerRussia.b__additional_algorithms.a_d__choice_machine_finance import choice_machine_finance


@dataclass
class _FinanceData:
    """
    Суть: Внутренний контейнер данных для хранения состояния генератора финансовых данных. Хранит
    сгенерированные финансовые компоненты (БИК, количество банковских карт, названия банков,
    номера карт, CVV/CVC коды, зарплата, типы карт, сроки действия карт, ИНН банков, КПП банков,
    наличие банкротства) для обеспечения согласованности данных при множественных обращениях к свойствам.
    """
    bik: str = None
    number_cards: int | str = None
    bank: List[str] | str = None
    bank_card: List[str] | str = None
    cvv_cvc: List[str] | str = None
    salary: int = None
    card_type: List[str] | str = None
    validity_period: List[str] | str = None
    inn_bank: List[str] | str = None
    kpp_bank: List[str] | str = None
    bankruptcy: bool = None


class FinanceGenerator(BaseGenerator):
    """
    Суть: Генератор финансовых данных человека. Предоставляет функциональность для генерации
    различных финансовых характеристик: БИК (банковский идентификационный код), количество банковских
    карт, названия банков, номера банковских карт (с корректной контрольной суммой по алгоритму Луна),
    CVV/CVC коды, размер зарплаты (в зависимости от должности и уровня работы), типы банковских
    карт, сроки действия карт, ИНН банков, КПП банков, наличие банкротства. Данные загружаются из
    JSON-файлов. Для генерации использует информацию из переданных генераторов биографии, адреса,
    документов и работы.
    """

    def __init__(self, bio, address, document, work):
        """
        Суть: Инициализация генератора финансовых данных. Создает экземпляр генератора, сохраняет ссылки
        на генераторы биографии (bio), адреса (address), документов (document) и работы (work) для
        использования их данных. Инициализирует внутреннее хранилище данных _FinanceData и загружает
        финансовые данные из JSON-файлов через метод _load_finance_data.
        """
        super().__init__()
        self._bio = bio
        self._address = address
        self._document = document
        self._work = work
        self._data = _FinanceData()
        self._load_finance_data()

    def _load_finance_data(self):
        """
        Суть: Загрузка финансовых данных из JSON-файлов. Загружает данные о банках из файла
        'a__data/bank/banks.json'. Сохраняет загруженные данные в атрибут BANKS для дальнейшего
        использования. Словарь BANKS содержит названия банков и соответствующие им ИНН и КПП.
        """
        banks_data = self._load_json('a__data/bank/banks.json')
        self.BANKS = banks_data.get("BANKS", [])

    def reset(self):
        """
        Суть: Сброс сгенерированных финансовых данных. Очищает внутреннее хранилище данных,
        создавая новый экземпляр _FinanceData, что позволяет сгенерировать новый набор финансовых
        компонентов при последующих обращениях к свойствам.
        """
        self._data = _FinanceData()
        return "Финансовые данные сброшены"

    @property
    @handle_errors
    def bik(self) -> str:
        """
        Суть: Получение БИК (банковского идентификационного кода). Для лиц младше AGE_FOR_CARD
        возвращает соответствующий ответ из SMALL_AGE_ANSWERS[9]. Для остальных формирует БИК в
        формате "04XXXXXYYYYY". Первые 2 цифры всегда "04" (код России). Следующие 2 цифры - код
        региона из PASSPORT_REGION_CODES по городу (если не найден, используется "00"). Затем 1
        случайная цифра от 0 до 9. Последние 3 цифры - случайное число от 100 до 999. Результат
        сохраняется во внутреннем хранилище.
        """
        if self._data.bik is None:
            if self._bio.age < self.AGE_FOR_CARD:
                self._data.bik = self.SMALL_AGE_ANSWERS[9]
            else:
                region_code = self._document.PASSPORT_REGION_CODES.get(self._address.city, "00")
                self._data.bik = f"04{region_code}0{random.randint(0, 9)}{random.randint(100, 999)}"
        return self._data.bik

    @property
    @handle_errors
    def number_cards(self) -> int | str:
        """
        Суть: Получение количества банковских карт. Для лиц младше AGE_FOR_CARD возвращает
        соответствующий ответ из SMALL_AGE_ANSWERS[10]. Для остальных с вероятностью 50% возвращает 0,
        иначе возвращает случайное число от 1 до 5. Результат сохраняется во внутреннем хранилище.
        """
        if self._data.number_cards is None:
            if self._bio.age < self.AGE_FOR_CARD:
                self._data.number_cards = self.SMALL_AGE_ANSWERS[10]
                return self._data.number_cards
            if random.choice([True, False]):
                self._data.number_cards = 0
            else:
                self._data.number_cards = random.randint(1, 5)
        return self._data.number_cards

    @handle_errors
    def bank(self, visualization: bool = False) -> List[str] | str:
        """
        Суть: Получение списка названий банков. Для лиц младше AGE_FOR_CARD возвращает соответствующий
        ответ из SMALL_AGE_ANSWERS[10]. Для остальных генерирует список названий банков длиной, равной
        количеству карт (number_cards). Названия банков выбираются случайным образом из ключей словаря
        BANKS. Если параметр visualization=True, возвращает строку с элементами через запятую, иначе
        возвращает список. Результат сохраняется во внутреннем хранилище.
        """
        if self._data.bank is None:
            if self._bio.age < self.AGE_FOR_CARD:
                self._data.bank = self.SMALL_AGE_ANSWERS[10]
            else:
                banks = [random.choice(list(self.BANKS.keys())) for _ in range(self.number_cards)]
                self._data.bank = banks
        if visualization:
            return ", ".join(self._data.bank)
        return self._data.bank

    @handle_errors
    def bank_card(self, visualization: bool = False) -> List[str] | str:
        """
        Суть: Получение списка номеров банковских карт. Для лиц младше AGE_FOR_CARD возвращает
        соответствующий ответ из SMALL_AGE_ANSWERS[10]. Для остальных генерирует номера карт длиной,
        равной количеству карт (number_cards). Номер карты формируется по алгоритму Луна:
        PREFIX (6 цифр) + 11 случайных цифр + контрольная цифра. Контрольная цифра вычисляется по
        алгоритму: цифры на четных позициях удваиваются, если результат больше 9, вычитается 9,
        затем все суммируется, контрольная цифра = (10 - (сумма % 10)) % 10. Если параметр
        visualization=True, возвращает строку с элементами через запятую, иначе возвращает список.
        Результат сохраняется во внутреннем хранилище.
        """
        if self._data.bank_card is None:
            if self._bio.age < self.AGE_FOR_CARD:
                self._data.bank_card = self.SMALL_AGE_ANSWERS[10]
            else:
                lst_bank_card = []
                for card in range(self.number_cards):
                    eleven = str(random.randint(10000, 99999999999)).zfill(11)
                    card = list(self.PREFIX + eleven)
                    total = 0
                    for i, digit in enumerate(card):
                        num = int(digit)
                        if (i + 1) % 2 == 0:
                            num *= 2
                            if num > 9:
                                num -= 9
                        total += num
                    checksum = (10 - (total % 10)) % 10
                    text = f"{self.PREFIX}{eleven}{checksum}"
                    lst_bank_card.append(text)
                self._data.bank_card = lst_bank_card
        if visualization:
            return ", ".join(self._data.bank_card)
        return self._data.bank_card

    @handle_errors
    def cvv_cvc(self, visualization: bool = False) -> List[str] | str:
        """
        Суть: Получение списка CVV/CVC кодов банковских карт. Для лиц младше AGE_FOR_CARD возвращает
        соответствующий ответ из SMALL_AGE_ANSWERS[10]. Для остальных генерирует список трехзначных
        CVV/CVC кодов (от 100 до 999) длиной, равной количеству карт (number_cards). Если параметр
        visualization=True, возвращает строку с элементами через запятую, иначе возвращает список.
        Результат сохраняется во внутреннем хранилище.
        """
        if self._data.cvv_cvc is None:
            if self._bio.age < self.AGE_FOR_CARD:
                self._data.cvv_cvc = self.SMALL_AGE_ANSWERS[10]
            else:
                lst_cvv = [f"{random.randint(100, 999):03d}" for _ in range(self.number_cards)]
                self._data.cvv_cvc = lst_cvv
        if visualization:
            return ", ".join(self._data.cvv_cvc)
        return self._data.cvv_cvc

    @property
    @handle_errors
    def salary(self) -> int:
        """
        Суть: Получение размера зарплаты. Если человек трудоустроен (self._work.is_employed),
        определяет зарплату на основе должности и уровня работы. Из словаря JOBS по названию
        должности получает диапазон зарплат, соответствующий уровню работы (self._work.level_work).
        Зарплата выбирается случайно в этом диапазоне. Если человек не трудоустроен, возвращает 0.
        Результат сохраняется во внутреннем хранилище.
        """
        if self._data.salary is None:
            if self._work.is_employed:
                job = self._work.JOBS[self._work.job]
                index_job = self.LEVEL_WORK.index(self._work.level_work)
                self._data.salary = random.randint(job[index_job][0], job[index_job][1])
            else:
                self._data.salary = 0
        return self._data.salary

    @handle_errors
    def card_type(self, visualization: bool = False) -> List[str] | str:
        """
        Суть: Получение списка типов банковских карт. Для лиц младше AGE_FOR_CARD возвращает
        соответствующий ответ из SMALL_AGE_ANSWERS[10]. Для остальных генерирует список типов карт
        (например, "Debit", "Credit") длиной, равной количеству карт (number_cards). Типы выбираются
        случайным образом из списка CARD_TYPE. Если параметр visualization=True, возвращает строку с
        элементами через запятую, иначе возвращает список. Результат сохраняется во внутреннем хранилище.
        """
        if self._data.card_type is None:
            if self._bio.age < self.AGE_FOR_CARD:
                self._data.card_type = self.SMALL_AGE_ANSWERS[10]
            else:
                lst_type_card = [random.choice(self.CARD_TYPE) for _ in range(self.number_cards)]
                self._data.card_type = lst_type_card
        if visualization:
            return ", ".join(self._data.card_type)
        return self._data.card_type

    @handle_errors
    def validity_period(self, visualization: bool = False) -> List[str] | str:
        """
        Суть: Получение списка сроков действия банковских карт. Для лиц младше AGE_FOR_CARD
        возвращает соответствующий ответ из SMALL_AGE_ANSWERS[10]. Для остальных генерирует
        список сроков действия длиной, равной количеству карт (number_cards). Каждый срок
        действия формируется в формате "MM/YY": месяц от 1 до 12 с ведущим нулем, год от 2015
        до (текущий год + 8) с двумя последними цифрами. Если параметр visualization=True,
        возвращает строку с элементами через запятую, иначе возвращает список. Результат
        сохраняется во внутреннем хранилище.
        """
        if self._data.validity_period is None:
            if self._bio.age < self.AGE_FOR_CARD:
                self._data.validity_period = self.SMALL_AGE_ANSWERS[10]
            else:
                lst_date = []
                for _ in range(self.number_cards):
                    month = f"{random.randint(1, 12):02d}"
                    year = f"{random.randint(2015, datetime.now().year + 8) % 100:02d}"
                    lst_date.append(f"{month}/{year}")
                self._data.validity_period = lst_date
        if visualization:
            return ", ".join(self._data.validity_period)
        return self._data.validity_period

    @handle_errors
    def inn_bank(self) -> List[str] | str:
        """
        Суть: Получение списка ИНН банков. Для лиц младше AGE_FOR_CARD возвращает
        соответствующий ответ из SMALL_AGE_ANSWERS[10]. Для остальных возвращает
        список ИНН банков, соответствующих названиям банков из свойства bank. ИНН
        извлекаются из словаря BANKS. Использует вспомогательную функцию choice_machine_finance
        с параметром variant=0.
        """
        return choice_machine_finance(
            inn_kpp_bank=self._data.inn_bank,
            age=self._bio.age,
            age_for_card=self.AGE_FOR_CARD,
            small_age=self.SMALL_AGE_ANSWERS,
            banks=self.bank(),
            bank_var=self.BANKS,
            variant=0
        )

    @handle_errors
    def kpp_bank(self) -> List[str] | str:
        """
        Суть: Получение списка КПП банков. Для лиц младше AGE_FOR_CARD возвращает соответствующий
        ответ из SMALL_AGE_ANSWERS[10]. Для остальных возвращает список КПП банков, соответствующих
        названиям банков из свойства bank. КПП извлекаются из словаря BANKS. Использует
        вспомогательную функцию choice_machine_finance с параметром variant=1.
        """
        return choice_machine_finance(
            inn_kpp_bank=self._data.kpp_bank,
            age=self._bio.age,
            age_for_card=self.AGE_FOR_CARD,
            small_age=self.SMALL_AGE_ANSWERS,
            banks=self.bank(),
            bank_var=self.BANKS,
            variant=1
        )

    @property
    def bankruptcy(self) -> bool:
        """
        Суть: Получение статуса банкротства. Для лиц младше 18 лет всегда возвращает False
        (несовершеннолетние не могут быть признаны банкротами). Для совершеннолетних
        случайным образом выбирает True или False с вероятностью 50%. Результат сохраняется
        во внутреннем хранилище.
        """
        if self._data.bankruptcy is None:
            if self._bio.age < 18:
                self._data.bankruptcy = False
            self._data.bankruptcy = random.choice([True, False])
        return self._data.bankruptcy

    def __str__(self) -> str:
        """
        Суть: Строковое представление всех сгенерированных финансовых данных. Формирует
        многострочную строку, содержащую все финансовые компоненты: БИК, количество карт,
        названия банков, ИНН банков, КПП банков, номера карт, CVV/CVC коды, типы карт,
        сроки действия, зарплату, наличие банкротства. Используется для удобного вывода
        всей информации о сгенерированных финансовых данных.
        """
        return (f"БИК: {self.bik}\n"
                f"Количество карт: {self.number_cards}\n"
                f"Банки: {self.bank()}\n"
                f"ИНН банков: {self.inn_bank()}\n"
                f"КПП банков: {self.kpp_bank()}\n"
                f"Номера карт: {self.bank_card()}\n"
                f"CVV/CVC: {self.cvv_cvc()}\n"
                f"Типы карт: {self.card_type()}\n"
                f"Сроки действия: {self.validity_period()}\n"
                f"Зарплата: {self.salary}\n"
                f"Банкротство: {self.bankruptcy}")