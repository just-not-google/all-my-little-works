from russiafaker.b_a__address_generator import AddressGenerator
from russiafaker.b_b__bio_generator import BioGenerator
from russiafaker.b_c__contact_generator import ContactGenerator
from russiafaker.b_d__document_generator import DocumentGenerator
from russiafaker.b_e__finance_generator import FinanceGenerator
from russiafaker.b_f__work_generator import WorkGenerator
from russiafaker.b_g__vehicle_generator import VehicleGenerator
from russiafaker.b_i__family_generator import FamilyGenerator


class PersonData:
    """
    Суть: Контейнер для хранения всех сгенерированных данных о человеке.
    Предоставляет прямой доступ ко всем атрибутам без необходимости
    обращаться к отдельным генераторам.
    """
    def __init__(self, bio, address, document, contact, work, finance, vehicle, family):
        self.full_name = bio.full_name
        self.name = bio.name
        self.surname = bio.surname
        self.patronymic = bio.patronymic
        self.gender = bio.gender
        self.age = bio.age
        self.birth_date = bio.year
        self.nationality = bio.nationality
        self.height = bio.height
        self.weight = bio.weight
        self.body_mass_index = bio.body_mass_index
        self.zodiac_sign = bio.zodiac_sign
        self.generation = bio.generation
        self.blood_type = bio.blood_type
        self.religion = bio.religion
        self.body_type = bio.body_type
        self.eye_color = bio.eye_color
        self.hair_color = bio.hair_color
        self.education_level = bio.education_level
        self.average_score_certificate = bio.average_score_certificate
        self.current_place_study = bio.current_place_study
        self.shoe_size = bio.shoe_size
        self.vision = bio.vision
        self.hearing_status = bio.hearing_status
        self.disability_group = bio.disability_group
        self.pulse = bio.pulse
        self.vaccinations = bio.vaccinations()
        self.military_fitness_category = bio.military_fitness_category
        self.father_full_name = bio.full_name_father
        self.mother_full_name = bio.full_name_mother
        self.region = address.region
        self.city = address.city
        self.street = address.street
        self.registration_address = address.registration_address
        self.actual_address = address.actual_address
        self.housing_type = address.housing_type
        self.phone = contact.phone
        self.mobile_operator = contact.mobile_operator
        self.phone_model = contact.phone_model
        self.email = contact.email
        self.social_networks = contact.social_networks()
        self.ipv4 = contact.ipv4
        self.ipv6 = contact.ipv6
        self.gaming_platform = contact.gaming_platform
        self.inn = document.inn
        self.snils = document.snils
        self.passport = document.passport_series_number
        self.passport_issue_date = document.date_issue
        self.passport_unit_code = document.unit_code
        self.enp = document.enp
        self.administrative_violations = document.administrative_violations()
        self.is_employed = work.is_employed
        self.job = work.job
        self.work_experience = work.work_experience
        self.job_start_date = work.job_start_date
        self.level_work = work.level_work
        self.place_work = work.place_work
        self.diseases = work.diseases()
        self.bad_habits = work.bad_habits()
        self.hobby = work.hobby()
        self.english_level = work.english_level
        self.work_schedule = work.work_schedule
        self.bik = finance.bik
        self.number_cards = finance.number_cards
        self.banks = finance.bank()
        self.bank_inn = finance.inn_bank()
        self.bank_kpp = finance.kpp_bank()
        self.bank_cards = finance.bank_card()
        self.cvv_cvc = finance.cvv_cvc()
        self.card_types = finance.card_type()
        self.card_validity = finance.validity_period()
        self.salary = finance.salary
        self.bankruptcy = finance.bankruptcy
        self.has_car = vehicle.has_car
        self.car = vehicle.car
        self.car_body_type = vehicle.car_body_type
        self.car_engine_type = vehicle.machine_engine_type
        self.car_engine_capacity = vehicle.engine_capacity
        self.car_transmission = vehicle.transmission_type
        self.car_drive = vehicle.machine_drive
        self.car_engine_power = vehicle.engine_power
        self.car_reg_number = vehicle.car_registration_number
        self.car_condition = vehicle.car_condition_type()
        self.car_color = vehicle.car_color
        self.car_year = vehicle.car_year
        self.marital_status = family.marital_status
        self.spouse_full_name = family.spouse_full_name
        self.spouse_age = family.spouse_age
        self.marriage_date = family.marriage_date
        self.years_marriage = family.years_marriage
        self.children_count = family.children_count
        self.children_names = family.children_names()
        self.living_with_parents = family.living_with_parents
        self.family_members_count = family.family_members_count

    def to_dict(self) -> dict:
        """
        Суть: Преобразование всех данных в словарь.
        Удобно для сохранения в JSON или другие форматы.
        """
        return {
            'full_name': self.full_name,
            'name': self.name,
            'surname': self.surname,
            'patronymic': self.patronymic,
            'gender': self.gender,
            'age': self.age,
            'birth_date': self.birth_date,
            'nationality': self.nationality,
            'height': self.height,
            'weight': self.weight,
            'body_mass_index': self.body_mass_index,
            'zodiac_sign': self.zodiac_sign,
            'generation': self.generation,
            'blood_type': self.blood_type,
            'religion': self.religion,
            'body_type': self.body_type,
            'eye_color': self.eye_color,
            'hair_color': self.hair_color,
            'education_level': self.education_level,
            'average_score_certificate': self.average_score_certificate,
            'current_place_study': self.current_place_study,
            'shoe_size': self.shoe_size,
            'vision': self.vision,
            'hearing_status': self.hearing_status,
            'disability_group': self.disability_group,
            'pulse': self.pulse,
            'vaccinations': self.vaccinations,
            'military_fitness_category': self.military_fitness_category,
            'father_full_name': self.father_full_name,
            'mother_full_name': self.mother_full_name,
            'region': self.region,
            'city': self.city,
            'street': self.street,
            'registration_address': self.registration_address,
            'actual_address': self.actual_address,
            'housing_type': self.housing_type,
            'phone': self.phone,
            'mobile_operator': self.mobile_operator,
            'phone_model': self.phone_model,
            'email': self.email,
            'social_networks': self.social_networks,
            'ipv4': self.ipv4,
            'ipv6': self.ipv6,
            'gaming_platform': self.gaming_platform,
            'inn': self.inn,
            'snils': self.snils,
            'passport': self.passport,
            'passport_issue_date': self.passport_issue_date,
            'passport_unit_code': self.passport_unit_code,
            'enp': self.enp,
            'administrative_violations': self.administrative_violations,
            'is_employed': self.is_employed,
            'job': self.job,
            'work_experience': self.work_experience,
            'job_start_date': self.job_start_date,
            'level_work': self.level_work,
            'place_work': self.place_work,
            'diseases': self.diseases,
            'bad_habits': self.bad_habits,
            'hobby': self.hobby,
            'english_level': self.english_level,
            'work_schedule': self.work_schedule,
            'bik': self.bik,
            'number_cards': self.number_cards,
            'banks': self.banks,
            'bank_inn': self.bank_inn,
            'bank_kpp': self.bank_kpp,
            'bank_cards': self.bank_cards,
            'cvv_cvc': self.cvv_cvc,
            'card_types': self.card_types,
            'card_validity': self.card_validity,
            'salary': self.salary,
            'bankruptcy': self.bankruptcy,
            'has_car': self.has_car,
            'car': self.car,
            'car_body_type': self.car_body_type,
            'car_engine_type': self.car_engine_type,
            'car_engine_capacity': self.car_engine_capacity,
            'car_transmission': self.car_transmission,
            'car_drive': self.car_drive,
            'car_engine_power': self.car_engine_power,
            'car_reg_number': self.car_reg_number,
            'car_condition': self.car_condition,
            'car_color': self.car_color,
            'car_year': self.car_year,
            'marital_status': self.marital_status,
            'spouse_full_name': self.spouse_full_name,
            'spouse_age': self.spouse_age,
            'marriage_date': self.marriage_date,
            'years_marriage': self.years_marriage,
            'children_count': self.children_count,
            'children_names': self.children_names,
            'living_with_parents': self.living_with_parents,
            'family_members_count': self.family_members_count,
        }

    def __str__(self) -> str:
        """Краткое строковое представление человека."""
        return (f"{self.full_name}, {self.age} лет, {self.gender}\n"
                f"Проживает: {self.registration_address}\n"
                f"Работа: {self.job}\n"
                f"Зарплата: {self.salary} руб.\n"
                f"Семейный статус: {self.marital_status}\n"
                f"Детей: {self.children_count}")


class FakerRussia:
    """
    Суть: Главный класс-агрегатор для генерации полного набора данных о человеке.
    Объединяет все специализированные генераторы (биографии, адреса, контактов,
    документов, финансов, работы, транспорта, семьи) в единый интерфейс. Предоставляет
    методы для генерации всех данных одновременно, сброса всех данных и вывода полной
    информации о сгенерированном человеке. При инициализации создает экземпляры всех
    дочерних генераторов, передавая между ними необходимые зависимости.
    """
    def __init__(self, my_gender: str = None):
        """
        Суть: Инициализация главного генератора FakerRussia. Создает экземпляры всех
        специализированных генераторов в правильном порядке с учетом их зависимостей.
        Сначала создается генератор биографии (bio) с возможностью указания пола,
        затем генератор адреса (address), затем генератор работы (work) с привязкой к
        биографии, затем генератор контактов (contact) с привязкой к биографии и
        адресу, затем генератор транспорта (vehicle) с привязкой к биографии и адресу,
        затем генератор документов (document) с привязкой к биографии, адресу и транспорту,
        затем генератор финансов (finance) с привязкой к биографии, адресу, документам и
        работе, затем генератор семьи (family) с привязкой к биографии и финансам. Все
        генераторы сохраняются как атрибуты класса для последующего доступа.
        """
        self.bio = BioGenerator(my_gender)
        self.address = AddressGenerator()
        self.work = WorkGenerator(self.bio)
        self.contact = ContactGenerator(self.bio, self.address)
        self.vehicle = VehicleGenerator(self.bio, self.address)
        self.document = DocumentGenerator(self.bio, self.address, self.vehicle)
        self.finance = FinanceGenerator(self.bio, self.address, self.document, self.work)
        self.family = FamilyGenerator(self.bio, self.finance)
        self._current_person = None

    def generate_person(self, reset_before: bool = True) -> PersonData:
        """
        Суть: Генерация полных данных о человеке.
        Аргументы: reset_before (bool): Если True, сначала сбрасывает все предыдущие данные.
        Возвращает: PersonData: Объект, содержащий все сгенерированные данные о человеке
        с удобным доступом к атрибутам.
        """
        if reset_before:
            self.reset()
        self._current_person = PersonData(
            bio=self.bio,
            address=self.address,
            document=self.document,
            contact=self.contact,
            work=self.work,
            finance=self.finance,
            vehicle=self.vehicle,
            family=self.family
        )
        return self._current_person

    def get_person(self) -> PersonData:
        """
        Суть: Получение последнего сгенерированного человека.
        Возвращает: PersonData: Объект с данными последнего сгенерированного
        человека или None, если ни одного человека еще не сгенерировано.
        """
        return self._current_person

    def reset(self):
        """
        Суть: Сброс всех сгенерированных данных. Вызывает метод reset у каждого из
        специализированных генераторов (bio, address, work, contact, document, finance,
        vehicle, family), очищая все внутренние хранилища данных. Возвращает сообщение
        об успешном сбросе всех данных. После сброса можно генерировать новый полный набор данных.
        """
        self.bio.reset()
        self.address.reset()
        self.work.reset()
        self.contact.reset()
        self.document.reset()
        self.finance.reset()
        self.vehicle.reset()
        self.family.reset()
        return "Все данные сброшены"

    def __str__(self):
        """
        Суть: Строковое представление полного набора данных о человеке. Объединяет строковые
        представления всех специализированных генераторов (bio, address, document, contact,
        work, finance, vehicle, family) в единую многострочную строку. Используется для удобного
        вывода всей информации о сгенерированном человеке в консоль или лог.
        """
        if self._current_person:
            return str(self._current_person)
        return (f"{self.bio}\n"
                f"{self.address}\n"
                f"{self.document}\n"
                f"{self.contact}\n"
                f"{self.work}\n"
                f"{self.finance}\n"
                f"{self.vehicle}\n"
                f"{self.family}")


if __name__ == "__main__":
    faker = FakerRussia()
    person = faker.generate_person()
    print("=" * 60)
    print(f"ФИО: {person.full_name}")
    print(f"Возраст: {person.age}")
    print(f"Телефон: {person.phone}")
    print(f"Email: {person.email}")
    print(f"Город: {person.city}")
    print(f"Адрес регистрации: {person.registration_address}")
    print(f"Работа: {person.job}")
    print(f"Зарплата: {person.salary} руб.")
    print(f"Семейный статус: {person.marital_status}")
    print(f"Автомобиль: {person.car}")
    print("=" * 60)
    print("\nВ виде словаря:")
    print(person.to_dict())
    print("\n" + "=" * 60)
    print("Генерация нового человека:")

    person2 = faker.generate_person()
    print(person2)
