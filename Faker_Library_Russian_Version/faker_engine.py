from datetime import datetime, timedelta
import random
import string
from typing import Dict, List, Optional, Tuple, Any
from enum import Enum
import uuid
from dataclasses import dataclass

from Faker_Library_Russian_Version.data.data import (house_types, card_types, educations, alphabet, sex,
                                                     region_codes, russian_alphabet, driver_license_category,
                                                     blood_group, rh_factor, email_domains, eye_color, hair_colors)
from Faker_Library_Russian_Version.data.data_man_names import man_names
from Faker_Library_Russian_Version.data.data_woman_names import woman_names
from Faker_Library_Russian_Version.data.data_man_surnames import man_surnames
from Faker_Library_Russian_Version.data.data_woman_surnames import woman_surnames
from Faker_Library_Russian_Version.data.data_man_patronymics import man_patronymics
from Faker_Library_Russian_Version.data.data_woman_patronymics import woman_patronymics
from Faker_Library_Russian_Version.data.data_random_words import random_words
from Faker_Library_Russian_Version.data.data_regions_cities_streets import regions
from Faker_Library_Russian_Version.data.data_banks import banks
from Faker_Library_Russian_Version.data.data_operators import operators
from Faker_Library_Russian_Version.data.data_jobs import jobs
from Faker_Library_Russian_Version.data.data_companies import companies
from Faker_Library_Russian_Version.data.data_universities import universities
from Faker_Library_Russian_Version.data.data_colleges import colleges


class Gender(Enum):
    MALE = "мужской"
    FEMALE = "женский"


@dataclass
class Person:
    full_name: str
    birth_date: str
    gender: str
    inn: str
    snils: str
    passport_series: int
    passport_number: int
    address: str
    phone: str
    email: str


class Russian_Faker:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, seed: Optional[int] = None, locale: str = "ru_RU"):
        if hasattr(self, '_initialized'):
            return
            
        self.seed = seed
        self.locale = locale
        if seed:
            random.seed(seed)
            
        self.now_date = datetime.now().date()
        self._cache = {}
        self._person = None
        self._initialized = True
        self._initialize_cache()

    def _initialize_cache(self):
        self._cache.update({
            'gender': random.choice(list(Gender)),
            'age': random.randint(18, 80),
            'birth_date': None,
            'name': None,
            'surname': None,
            'patronymic': None,
            'region': None,
            'city': None,
            'street': None,
            'passport_data': None,
            'driver_license_data': None
        })

    def _generate_checksum(self, digits: List[int], weights: List[int]) -> int:
        total = sum(d * w for d, w in zip(digits, weights))
        return total % 11 % 10

    def _calculate_inn_checksum(self, inn_base: str) -> str:
        coefficients_11 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
        coefficients_12 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
        
        digits = [int(d) for d in inn_base]
        
        checksum_11 = self._generate_checksum(digits, coefficients_11)
        digits.append(checksum_11)
        checksum_12 = self._generate_checksum(digits, coefficients_12)
        
        return f"{checksum_11}{checksum_12}"

    def _calculate_ogrn_checksum(self, ogrn_base: str) -> int:
        return int(ogrn_base) % 11 % 10

    def _generate_birth_date(self, age: int) -> datetime:
        birth_year = self.now_date.year - age
        month = random.randint(1, 12)
        
        if month == 2:
            day = random.randint(1, 28)
        elif month in [4, 6, 9, 11]:
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 31)
            
        return datetime(birth_year, month, day)

    def _safe_execute(self, func, default=None, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            return default if default is not None else "Ошибка генерации"

    def reset(self) -> 'Russian_Faker':
        self._initialize_cache()
        self._person = None
        return self

    def with_gender(self, gender: Gender) -> 'Russian_Faker':
        self._cache['gender'] = gender
        self._cache['name'] = None
        self._cache['surname'] = None
        self._cache['patronymic'] = None
        return self

    def with_age(self, age: int) -> 'Russian_Faker':
        self._cache['age'] = age
        self._cache['birth_date'] = None
        return self

    def with_birth_date(self, birth_date: str) -> 'Russian_Faker':
        self._cache['birth_date'] = datetime.strptime(birth_date, "%Y.%m.%d")
        return self

    def with_region(self, region: str) -> 'Russian_Faker':
        self._cache['region'] = region
        self._cache['city'] = None
        self._cache['street'] = None
        return self

    @property
    def current_gender(self) -> Gender:
        return self._cache['gender']

    @property
    def current_age(self) -> int:
        return self._cache['age']

    def datetime_between(self, start_date: str, end_date: str) -> datetime:
        start = datetime.strptime(start_date, "%Y.%m.%d")
        end = datetime.strptime(end_date, "%Y.%m.%d")
        delta = end - start
        random_days = random.randint(0, delta.days)
        return start + timedelta(days=random_days)

    def date_between(self, start_date: str, end_date: str) -> str:
        return self.datetime_between(start_date, end_date).strftime("%Y.%m.%d")

    def future_date(self, years: int = 1) -> str:
        future = self.now_date + timedelta(days=365 * years)
        return future.strftime("%Y.%m.%d")

    def past_date(self, years: int = 1) -> str:
        past = self.now_date - timedelta(days=365 * years)
        return past.strftime("%Y.%m.%d")

    def random_element(self, elements: List[Any]) -> Any:
        return random.choice(elements)

    def random_elements(self, elements: List[Any], unique: bool = True, count: Optional[int] = None) -> List[Any]:
        if count is None:
            count = random.randint(1, len(elements))
        if unique:
            return random.sample(elements, min(count, len(elements)))
        return [random.choice(elements) for _ in range(count)]

    def random_int(self, min: int = 0, max: int = 9999) -> int:
        return random.randint(min, max)

    def random_digit(self) -> int:
        return random.randint(0, 9)

    def random_number(self, digits: int = 6) -> int:
        return random.randint(10**(digits-1), 10**digits - 1)

    def uuid4(self) -> str:
        return str(uuid.uuid4())

    def boolean(self) -> bool:
        return random.choice([True, False])

    def null_boolean(self) -> Optional[bool]:
        return random.choice([True, False, None])

    def word(self) -> str:
        return random.choice(random_words)

    def words(self, count: int = 3) -> List[str]:
        return [self.word() for _ in range(count)]

    def sentence(self, word_count: int = 6) -> str:
        words = self.words(word_count)
        return ' '.join(words).capitalize() + '.'

    def paragraph(self, sentence_count: int = 3) -> str:
        sentences = [self.sentence() for _ in range(sentence_count)]
        return ' '.join(sentences)

    def text(self, max_chars: int = 200) -> str:
        return self.paragraph()[:max_chars]

    def password(self, length: int = 10) -> str:
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(chars) for _ in range(length))

    def name(self) -> str:
        if self._cache['name'] is None:
            if self.current_gender == Gender.MALE:
                self._cache['name'] = random.choice(man_names)
            else:
                self._cache['name'] = random.choice(woman_names)
        return self._cache['name']

    def surname(self) -> str:
        if self._cache['surname'] is None:
            if self.current_gender == Gender.MALE:
                self._cache['surname'] = random.choice(man_surnames)
            else:
                self._cache['surname'] = random.choice(woman_surnames)
        return self._cache['surname']

    def patronymic(self) -> str:
        if self._cache['patronymic'] is None:
            if self.current_gender == Gender.MALE:
                self._cache['patronymic'] = random.choice(man_patronymics)
            else:
                self._cache['patronymic'] = random.choice(woman_patronymics)
        return self._cache['patronymic']

    def first_name(self) -> str:
        return self.name()

    def last_name(self) -> str:
        return self.surname()

    def middle_name(self) -> str:
        return self.patronymic()

    def full_name(self) -> str:
        return f"{self.surname()} {self.name()} {self.patronymic()}"

    def initials(self) -> str:
        return f"{self.surname()} {self.name()[0]}.{self.patronymic()[0]}."

    def prefix(self) -> str:
        return "г-н" if self.current_gender == Gender.MALE else "г-жа"

    def name_with_prefix(self) -> str:
        return f"{self.prefix()} {self.full_name()}"

    def birth_date(self) -> str:
        if self._cache['birth_date'] is None:
            self._cache['birth_date'] = self._generate_birth_date(self.current_age)
        return self._cache['birth_date'].strftime("%Y.%m.%d")

    def age(self) -> int:
        return self.current_age

    def gender(self) -> str:
        return self.current_gender.value

    def inn_individual(self) -> str:
        region_code = f"{random.randint(1, 92):02d}"
        tax_code = f"{random.randint(1, 99):02d}"
        record_number = f"{random.randint(1, 999999):06d}"
        inn_base = region_code + tax_code + record_number
        checksum = self._calculate_inn_checksum(inn_base)
        return inn_base + checksum

    def inn_legal(self) -> str:
        region_code = f"{random.randint(1, 92):02d}"
        tax_code = f"{random.randint(1, 99):02d}"
        record_number = f"{random.randint(1, 99999):05d}"
        inn_base = region_code + tax_code + record_number
        checksum = str(self._generate_checksum([int(d) for d in inn_base], [2, 4, 10, 3, 5, 9, 4, 6, 8]))
        return inn_base + checksum

    def kpp(self) -> str:
        region_code = f"{random.randint(1, 92):02d}"
        reason_code = f"{random.randint(1, 99):02d}"
        tax_office = f"{random.randint(1, 99):03d}"
        return region_code + reason_code + tax_office

    def ogrn(self) -> str:
        sign = random.choice(['1', '5'])
        year = f"{random.randint(0, 99):02d}"
        region = f"{random.randint(1, 92):02d}"
        number = f"{random.randint(1, 999999999):09d}"
        ogrn_base = sign + year + region + number
        checksum = str(self._calculate_ogrn_checksum(ogrn_base))
        return ogrn_base + checksum

    def ogrnip(self) -> str:
        sign = '3'
        year = f"{random.randint(0, 99):02d}"
        region = f"{random.randint(1, 92):02d}"
        number = f"{random.randint(1, 9999999999):010d}"
        ogrnip_base = sign + year + region + number
        checksum = str(int(ogrnip_base) % 13 % 10)
        return ogrnip_base + checksum

    def snils(self) -> str:
        number = f"{random.randint(1, 999999999):09d}"
        digits = [int(d) for d in number]
        total = sum((9 - i) * digit for i, digit in enumerate(digits))
        checksum = total % 101
        if checksum == 100:
            checksum = 0
        return f"{number[:3]}-{number[3:6]}-{number[6:9]} {checksum:02d}"

    def passport_series_number(self) -> Tuple[int, int]:
        if self._cache['passport_data'] is None:
            series = random.randint(1000, 9999)
            number = random.randint(100000, 999999)
            self._cache['passport_data'] = (series, number)
        return self._cache['passport_data']

    def passport_series(self) -> int:
        return self.passport_series_number()[0]

    def passport_number(self) -> int:
        return self.passport_series_number()[1]

    def passport_issue_date(self) -> str:
        birth_date = self._cache['birth_date'] or self._generate_birth_date(self.current_age)
        min_date = birth_date.replace(year=birth_date.year + 14)
        max_date = datetime.now()
        delta = max_date - min_date
        random_days = random.randint(0, delta.days)
        return (min_date + timedelta(days=random_days)).strftime("%Y.%m.%d")

    def department_code(self) -> str:
        return f"{random.randint(100, 990)}-{random.randint(100, 990)}"

    def driver_license_series_number(self) -> Tuple[int, int]:
        if self._cache['driver_license_data'] is None:
            series = random.randint(1000, 9999)
            number = random.randint(100000, 999999)
            self._cache['driver_license_data'] = (series, number)
        return self._cache['driver_license_data']

    def driver_license_series(self) -> int:
        return self.driver_license_series_number()[0]

    def driver_license_number(self) -> int:
        return self.driver_license_series_number()[1]

    def driver_license_categories(self) -> str:
        count = random.randint(1, min(5, len(driver_license_category)))
        categories = random.sample(driver_license_category, count)
        return ", ".join(categories)

    def driver_license_issue_date(self) -> str:
        min_age_date = self._generate_birth_date(self.current_age).replace(year=self._cache['birth_date'].year + 18)
        max_date = datetime.now()
        delta = max_date - min_age_date
        random_days = random.randint(0, delta.days)
        return (min_age_date + timedelta(days=random_days)).strftime("%Y.%m.%d")

    def medical_insurance_policy(self) -> str:
        return f"{random.randint(1000000000000000, 9999999999999999):016d}"

    def military_ticket(self) -> str:
        return f"{random.choice(russian_alphabet)}{random.choice(russian_alphabet)} {random.randint(1000000, 9999999):07d}"

    def blood_group(self) -> str:
        return f"{random.choice(blood_group)} {random.choice(rh_factor)}"

    def zodiac_sign(self) -> str:
        birth_date = self._cache['birth_date'] or self._generate_birth_date(self.current_age)
        day = birth_date.day
        month = birth_date.month
        
        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return "Овен"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return "Телец"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return "Близнецы"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return "Рак"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return "Лев"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return "Дева"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return "Весы"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return "Скорпион"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return "Стрелец"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            return "Козерог"
        elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return "Водолей"
        else:
            return "Рыбы"

    def chinese_zodiac(self) -> str:
        birth_year = (self._cache['birth_date'] or self._generate_birth_date(self.current_age)).year
        signs = ["Крыса", "Бык", "Тигр", "Кролик", "Дракон", "Змея", 
                "Лошадь", "Коза", "Обезьяна", "Петух", "Собака", "Свинья"]
        return signs[(birth_year - 4) % 12]

    def email(self) -> str:
        name_part = self.name().lower()
        patterns = [
            f"{name_part}.{self.surname().lower()}",
            f"{name_part}_{random.randint(1000, 9999)}",
            f"{self.surname().lower()}.{name_part}",
            f"{name_part}{random.randint(100, 999)}"
        ]
        username = random.choice(patterns)
        return f"{username}@{random.choice(email_domains)}"

    def phone_number(self) -> str:
        return f"+7 ({random.randint(900, 999)}) {random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(10, 99)}"

    def mobile_operator(self) -> str:
        return random.choice(operators)

    def region(self) -> str:
        if self._cache['region'] is None:
            self._cache['region'] = random.choice(list(regions.keys()))
        return self._cache['region']

    def city(self) -> str:
        if self._cache['city'] is None:
            region_name = self.region()
            self._cache['city'] = random.choice(list(regions[region_name].keys()))
        return self._cache['city']

    def street(self) -> str:
        if self._cache['street'] is None:
            region_name = self.region()
            city_name = self.city()
            self._cache['street'] = random.choice(regions[region_name][city_name])
        return self._cache['street']

    def house_number(self) -> str:
        return f"{random.choice(house_types)} {random.randint(1, 200)}"

    def apartment(self) -> str:
        return f"кв. {random.randint(1, 300)}"

    def postal_code(self) -> str:
        return f"{random.randint(100000, 199999):06d}"

    def address(self) -> str:
        return f"{self.postal_code()}, {self.region()}, г. {self.city()}, ул. {self.street()}, {self.house_number()}, {self.apartment()}"

    def bank_name(self) -> str:
        return random.choice(banks)

    def card_number(self) -> str:
        return f"{random.randint(4000, 4999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)}"

    def card_type(self) -> str:
        return random.choice(card_types)

    def card_expiry(self) -> str:
        return f"{random.randint(1, 12):02d}/{random.randint(2025, 2030)}"

    def cvv(self) -> str:
        return f"{random.randint(100, 999):03d}"

    def bank_account(self) -> str:
        return f"{random.randint(10000000000000000000, 99999999999999999999):020d}"

    def bik(self) -> str:
        return f"{random.randint(100000000, 999999999):09d}"

    def correspondent_account(self) -> str:
        return f"301{self.bank_account()[3:]}"

    def job_title(self) -> str:
        return random.choice(jobs)

    def company(self) -> str:
        return random.choice(companies)

    def profession(self) -> str:
        return self.job_title()

    def salary(self) -> int:
        return random.randint(30000, 300000)

    def education(self) -> str:
        return random.choice(educations)

    def university(self) -> str:
        return random.choice(universities)

    def college(self) -> str:
        return random.choice(colleges)

    def work_experience(self) -> str:
        experience_years = random.randint(0, self.current_age - 18)
        experience_months = random.randint(0, 11)
        return f"{experience_years} лет {experience_months} месяцев"

    def height(self) -> int:
        if self.current_gender == Gender.MALE:
            return random.randint(165, 200)
        else:
            return random.randint(155, 185)

    def weight(self) -> int:
        if self.current_gender == Gender.MALE:
            return random.randint(65, 120)
        else:
            return random.randint(50, 90)

    def eye_color(self) -> str:
        return random.choice(eye_color)

    def hair_color(self) -> str:
        return random.choice(hair_colors)

    def car_plate(self) -> str:
        return f"{random.choice(alphabet)}{random.randint(100, 999)}{random.choice(alphabet)}{random.choice(alphabet)} {random.choice(region_codes)}"

    def vehicle_certificate(self) -> str:
        return f"{random.randint(1000, 9999)} {random.randint(100000, 999999)}"

    def vin(self) -> str:
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(17))

    def car_brand(self) -> str:
        brands = ["Lada", "Kia", "Hyundai", "Toyota", "Volkswagen", "Skoda", 
                 "Renault", "Nissan", "BMW", "Mercedes", "Audi", "Ford"]
        return random.choice(brands)

    def car_model(self) -> str:
        models = ["Granta", "Vesta", "Rio", "Solaris", "Camry", "Polo", 
                 "Rapid", "Logan", "Almera", "X5", "C-Class", "A4", "Focus"]
        return random.choice(models)

    def ip_address(self) -> str:
        return ".".join(str(random.randint(1, 255)) for _ in range(4))

    def mac_address(self) -> str:
        return ":".join(f"{random.randint(0, 255):02x}" for _ in range(6))

    def user_agent(self) -> str:
        browsers = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        ]
        return random.choice(browsers)

    def create_person(self) -> Person:
        return Person(
            full_name=self.full_name(),
            birth_date=self.birth_date(),
            gender=self.gender(),
            inn=self.inn_individual(),
            snils=self.snils(),
            passport_series=self.passport_series(),
            passport_number=self.passport_number(),
            address=self.address(),
            phone=self.phone_number(),
            email=self.email()
        )

    def profile(self) -> Dict[str, Any]:
        return {
            'personal': {
                'full_name': self.full_name(),
                'birth_date': self.birth_date(),
                'age': self.age(),
                'gender': self.gender(),
                'inn': self.inn_individual(),
                'snils': self.snils(),
                'blood_group': self.blood_group(),
                'zodiac': self.zodiac_sign(),
                'chinese_zodiac': self.chinese_zodiac()
            },
            'passport': {
                'series': self.passport_series(),
                'number': self.passport_number(),
                'issue_date': self.passport_issue_date(),
                'department_code': self.department_code()
            },
            'driver_license': {
                'series': self.driver_license_series(),
                'number': self.driver_license_number(),
                'categories': self.driver_license_categories(),
                'issue_date': self.driver_license_issue_date()
            },
            'appearance': {
                'height': self.height(),
                'weight': self.weight(),
                'eye_color': self.eye_color(),
                'hair_color': self.hair_color()
            },
            'contacts': {
                'phone': self.phone_number(),
                'email': self.email(),
                'address': self.address()
            },
            'education': {
                'level': self.education(),
                'university': self.university(),
                'college': self.college()
            },
            'work': {
                'company': self.company(),
                'position': self.job_title(),
                'salary': self.salary(),
                'experience': self.work_experience()
            },
            'banking': {
                'bank': self.bank_name(),
                'card_number': self.card_number(),
                'card_type': self.card_type(),
                'card_expiry': self.card_expiry(),
                'cvv': self.cvv(),
                'account': self.bank_account()
            },
            'medical': {
                'policy': self.medical_insurance_policy()
            },
            'vehicle': {
                'plate': self.car_plate(),
                'certificate': self.vehicle_certificate(),
                'vin': self.vin(),
                'brand': self.car_brand(),
                'model': self.car_model()
            }
        }

    def generate_batch(self, count: int = 10) -> List[Dict[str, Any]]:
        return [self.reset().profile() for _ in range(count)]

    def json(self) -> str:
        import json
        return json.dumps(self.profile(), ensure_ascii=False, indent=2)

    def xml(self) -> str:
        profile = self.profile()
        xml_parts = ['<?xml version="1.0" encoding="UTF-8"?>', '<person>']
        
        def dict_to_xml(data, parent_tag):
            for key, value in data.items():
                if isinstance(value, dict):
                    xml_parts.append(f'<{key}>')
                    dict_to_xml(value, key)
                    xml_parts.append(f'</{key}>')
                else:
                    xml_parts.append(f'<{key}>{value}</{key}>')
        
        dict_to_xml(profile, 'person')
        xml_parts.append('</person>')
        return '\n'.join(xml_parts)
