import random
from typing import List
from dataclasses import dataclass
from .b_h__base_generator import BaseGenerator
from FakerRussia.b__additional_algorithms.a_a__handle_errors import handle_errors


@dataclass
class _ContactData:
    """
    Суть: Внутренний контейнер данных для хранения состояния генератора контактных данных.
    Хранит сгенерированные контактные компоненты (номер телефона, мобильный оператор, модель
    телефона, email, социальные сети, IPv4, IPv6, игровая платформа) для обеспечения
    согласованности данных при множественных обращениях к свойствам.
    """
    phone: str = None
    mobile_operator: str = None
    phone_model: str = None
    email: str = None
    social_networks: List[str] | str = None
    ipv4: str = None
    ipv6: str = None
    gaming_platform: str = None


class ContactGenerator(BaseGenerator):
    """
    Суть: Генератор контактных данных человека. Предоставляет функциональность для генерации
    различных контактных характеристик: номер телефона (с кодом города), мобильный оператор,
    модель телефона, email, список социальных сетей и мессенджеров, IPv4 и IPv6 адреса,
    игровая платформа. Данные загружаются из JSON-файлов. Для генерации телефонных данных
    использует информацию о городе из переданного генератора адресов, а для возрастных ограничений
    - данные из переданного генератора биографии.
    """

    def __init__(self, bio, address):
        """
        Суть: Инициализация генератора контактных данных. Создает экземпляр генератора, сохраняет
        ссылки на генераторы биографии (bio) и адреса (address) для использования их данных.
        Инициализирует внутреннее хранилище данных _ContactData и загружает контактные данные из
        JSON-файлов через метод _load_contact_data.
        """
        super().__init__()
        self._bio = bio
        self._address = address
        self._data = _ContactData()
        self._load_contact_data()

    def _load_contact_data(self):
        """
        Суть: Загрузка контактных данных из JSON-файлов. Загружает телефонные коды городов из
        файла 'a__data/phone/phone_code.json', модели телефонов из файла 'a__data/phone/phone_models.json',
        имена пользователей для email из файла 'a__data/email/email_usernames.json', домены email
        из файла 'a__data/email/email_domains.json', мобильные операторы из файла
        'a__data/mobile_operator/mobile_operators.json', социальные сети и мессенджеры
        из файла 'a__data/social_networks_messengers/social_networks_messengers.json'. Сохраняет
        загруженные данные в атрибуты класса для дальнейшего использования.
        """
        phone_data = self._load_json('a__data/phone/phone_code.json')
        self.PHONE_CODES = phone_data.get("PHONE_CODES", {})
        phone_models_data = self._load_json('a__data/phone/phone_models.json')
        self.PHONE_MODELS = phone_models_data.get("PHONE_MODELS", [])
        email_usernames_data = self._load_json('a__data/email/email_usernames.json')
        self.EMAIL_USERNAMES = email_usernames_data.get("EMAIL_USERNAMES", [])
        email_domains_data = self._load_json('a__data/email/email_domains.json')
        self.EMAIL_DOMAINS = email_domains_data.get("EMAIL_DOMAINS", [])
        mobile_operators_data = self._load_json('a__data/mobile_operator/mobile_operators.json')
        self.MOBILE_OPERATORS = mobile_operators_data.get("MOBILE_OPERATORS", [])
        social_data = self._load_json('a__data/social_networks_messengers/social_networks_messengers.json')
        self.SOCIAL_NETWORKS_AND_MESSENGERS = social_data.get("SOCIAL_NETWORKS_AND_MESSENGERS", [])

    def reset(self):
        """
        Суть: Сброс сгенерированных контактных данных. Очищает внутреннее хранилище данных,
        создавая новый экземпляр _ContactData, что позволяет сгенерировать новый набор
        контактных компонентов при последующих обращениях к свойствам.
        """
        self._data = _ContactData()
        return "Контактные данные сброшены"

    @property
    @handle_errors
    def phone(self) -> str:
        """
        Суть: Получение номера телефона. Для детей младше 6 лет возвращает соответствующий
        ответ из SMALL_AGE_ANSWERS[6]. Для остальных формирует номер телефона в формате:
        код страны (COUNTRY_CODE), код города (из PHONE_CODES по названию города из
        генератора адресов), затем три группы цифр: 100-999, 10-99, 10-99. Формат:
        "+7 (код) XXX-XX-XX". Результат сохраняется во внутреннем хранилище.
        """
        if self._data.phone is None:
            if self._bio.age < 6:
                self._data.phone = self.SMALL_AGE_ANSWERS[6]
            else:
                phone_code = self.PHONE_CODES[self._address.city]
                self._data.phone = (f"{self.COUNTRY_CODE} ({phone_code}) {random.randint(100, 999)}-"
                                    f"{random.randint(10, 99)}-{random.randint(10, 99)}")
        return self._data.phone

    @property
    @handle_errors
    def mobile_operator(self) -> str:
        """
        Суть: Получение мобильного оператора. Для детей младше 6 лет возвращает
        соответствующий ответ из SMALL_AGE_ANSWERS[6]. Для остальных возвращает
        случайного мобильного оператора из загруженного списка MOBILE_OPERATORS.
        Результат сохраняется во внутреннем хранилище.
        """
        if self._data.mobile_operator is None:
            if self._bio.age < 6:
                self._data.mobile_operator = self.SMALL_AGE_ANSWERS[6]
            else:
                self._data.mobile_operator = random.choice(self.MOBILE_OPERATORS)
        return self._data.mobile_operator

    @property
    @handle_errors
    def phone_model(self) -> str:
        """
        Суть: Получение модели телефона. Для детей младше 6 лет возвращает
        соответствующий ответ из SMALL_AGE_ANSWERS[7]. Для остальных возвращает
        случайную модель телефона из загруженного списка PHONE_MODELS. Результат
        сохраняется во внутреннем хранилище.
        """
        if self._data.phone_model is None:
            if self._bio.age < 6:
                self._data.phone_model = self.SMALL_AGE_ANSWERS[7]
            else:
                self._data.phone_model = random.choice(self.PHONE_MODELS)
        return self._data.phone_model

    @property
    @handle_errors
    def email(self) -> str:
        """
        Суть: Получение email адреса. Формирует email в формате "имя_пользователя@домен".
        Имя пользователя выбирается случайно из списка EMAIL_USERNAMES, домен - из списка
        EMAIL_DOMAINS. Результат сохраняется во внутреннем хранилище.
        """
        if self._data.email is None:
            self._data.email = f"{random.choice(self.EMAIL_USERNAMES)}@{random.choice(self.EMAIL_DOMAINS)}"
        return self._data.email

    @handle_errors
    def social_networks(self, visualization: bool = False) -> List[str] | str:
        """
        Суть: Получение списка социальных сетей и мессенджеров. Генерирует случайный
        список из 1-15 уникальных социальных сетей/мессенджеров из загруженного списка
        SOCIAL_NETWORKS_AND_MESSENGERS. Если параметр visualization=True, возвращает
        строку с элементами через запятую, иначе возвращает список. Результат
        сохраняется во внутреннем хранилище.
        """
        if self._data.social_networks is None:
            selected = []
            for _ in range(random.randint(1, 15)):
                net = random.choice(self.SOCIAL_NETWORKS_AND_MESSENGERS)
                if net not in selected:
                    selected.append(net)
            self._data.social_networks = selected
        if visualization:
            return ", ".join(self._data.social_networks)
        return self._data.social_networks

    @property
    @handle_errors
    def ipv4(self) -> str:
        """
        Суть: Получение IPv4 адреса. Генерирует случайный IPv4 адрес в формате
        "X.X.X.X", где каждая часть (октет) - случайное число от 1 до 255.
        Результат сохраняется во внутреннем хранилище.
        """
        if self._data.ipv4 is None:
            parts = [str(random.randint(1, 255)) for _ in range(4)]
            self._data.ipv4 = ".".join(parts)
        return self._data.ipv4

    @property
    @handle_errors
    def ipv6(self) -> str:
        """
        Суть: Получение IPv6 адреса. Генерирует случайный IPv6 адрес в
        формате "XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX", где каждая
        группа состоит из 4 случайных символов из набора STRING_IPv6
        (шестнадцатеричные цифры). Результат сохраняется во внутреннем хранилище.
        """
        if self._data.ipv6 is None:
            parts = ["".join(random.choices(self.STRING_IPv6, k=4)) for _ in range(8)]
            self._data.ipv6 = ":".join(parts)
        return self._data.ipv6

    @property
    @handle_errors
    def gaming_platform(self) -> str:
        """
        Суть: Получение игровой платформы. Для детей младше 4 лет возвращает
        соответствующий ответ из SMALL_AGE_ANSWERS[11]. Для остальных с вероятностью
        50% возвращает "Данный человек не играет в видеоигры". В противном случае
        возвращает случайную игровую платформу из загруженного списка GAMING_PLATFORMS.
        Результат сохраняется во внутреннем хранилище.
        """
        if self._data.gaming_platform is None:
            if self._bio.age < 4:
                self._data.gaming_platform = self.SMALL_AGE_ANSWERS[11]
                return self._data.gaming_platform
            if random.choice([True, False]):
                self._data.gaming_platform = "Данный человек не играет в видеоигры"
                return self._data.gaming_platform
            self._data.gaming_platform = random.choice(self.GAMING_PLATFORMS)
        return self._data.gaming_platform

    def __str__(self):
        """
        Суть: Строковое представление всех сгенерированных контактных данных.
        Формирует многострочную строку, содержащую все контактные компоненты:
        номер телефона, мобильный оператор, модель телефона, email, социальные
        сети, IPv4, IPv6, игровая платформа. Используется для удобного вывода
        всей информации о сгенерированных контактных данных.
        """
        return (f"Номер телефона: {self.phone}\n"
                f"Мобильный оператор: {self.mobile_operator}\n"
                f"Модель телефона: {self.phone_model}\n"
                f"Email: {self.email}\n"
                f"Социальные сети: {self.social_networks()}\n"
                f"IPv4: {self.ipv4}\n"
                f"IPv6: {self.ipv6}\n"
                f"Игровая платформа: {self.gaming_platform}")